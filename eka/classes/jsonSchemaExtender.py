r"""
Extensions over JSON Schema's validator, to allow for mutations, like default values etc.
"""
from jsonschema import Draft4Validator, validators

# Helpers
def extend(validator_class):
  validate_properties = validator_class.VALIDATORS['properties']

  def mutateInstance(validator, properties, instance, schema):
    # Set the defaults. #Note: In cases of multiple schema matches, the last default (among all matching schemas), will be used.
    for property, subschema in properties.iteritems():
      if not hasattr(instance, 'iteritems'):
        return

      if 'default' in subschema:
        # instance.setdefault(property, subschema['default']) # #Note: This makes the first default to be chosen. The issue is that, it fails to process the anyOf directives properly.
        instance[property] = subschema['default']

    for error in validate_properties(
      validator, properties, instance, schema,
    ):
      yield error

  return validators.extend(
    validator_class, {'properties' : mutateInstance},
  )

# Exports
ExtendedDraft4Validator = extend(Draft4Validator)
