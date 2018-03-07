r"""
Extensions over JSON Schema's validator, to allow for mutations, like default values etc.
"""
from jsonschema import Draft4Validator, validators
from jsonschema.exceptions import ValidationError

# Helpers
def extend(validator_class):
  validate_properties = validator_class.VALIDATORS['properties']

  def mutateInstance(validator, properties, instance, schema):
    # Set the defaults. #Note: In cases of multiple schema matches, the last default (among all matching schemas), will be used.
    for property, subschema in properties.iteritems():
      if not hasattr(instance, 'iteritems'):
        return

      if 'default' in subschema:
        instance.setdefault(property, subschema['default'])

      elif 'required' in subschema and type(subschema['required']) == bool: # #Note: This is the extension, which overrideds the property required, to use booleans on self, rathen than a list for the properties children.
        required = subschema['required']
        del subschema['required']
        if required and not property in instance:
          yield ValidationError('Required property \'%s\' is not provided' % property, instance=isinstance, schema=subschema)

    for error in validate_properties(validator, properties, instance, schema):
      yield error

  return validators.extend(
    validator_class, {'properties' : mutateInstance},
  )

# Exports
ExtendedDraft4Validator = extend(Draft4Validator)
