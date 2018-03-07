r"""
The base parser for crud applications.
"""

from eka.classes.node import node
from eka.classes.ymlParser import parseYML
from eka.helpers import isMap
from eka.plugins import define, getPluginClass

# Data
Definitions = parseYML(r"""
crud.app:
  allOf:
    - properties:
        class:
          default: crud.app
        buildBase:
          type: string
          required: true
        builder:
          $ref: '#/definitions/object'
          required: true
        props:
          type: object
          patternProperties:
            '^([A-z0-9_-])+$':
              $ref: '#/definitions/crud.resource'
    - $ref: '#/definitions/providable'
    - $ref: '#/definitions/object'

crud.resource:
  allOf:
    - type: object
      properties:
        class:
          enum: [crud.resource]
          default: crud.resource
        permissions:
          type: string
          default: crud
          pattern: '^[crud]+|all|none|$'
        props:
          type: object
          patternProperties:
            '^([A-z0-9_-])+$':
              $ref: '#/definitions/crud.field'
    - $ref: '#/definitions/providable'

crud.field:
  allOf:
    - anyOf:
      - type: [integer, string]
      - type: object
        properties:
            class:
              enum: [crud.field]
              default: crud.field
            value:
              type: [integer, string]
    - $ref: '#/definitions/providable'
""")

# Helpers
def getSchemaExtension(className):
  Schema = {'definitions': Definitions}
  Schema.update(Definitions[className])

  return Schema

@define('crud.app')
class app(node):
  r"""A class to process structures of type, crud.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('crud.app'))

  def build(self):
    getPluginClass(self.Structure['builder']['class'])(self.Structure, self.Scopes).build()

@define('crud.resource')
class resource(node):
  r"""A class to process structures of type, crud.resource.
  """
  __DefaultProperties__ = {
    'permissions': 'crud',
  }
  __Data__ = {
    'permissions': {
      'all': 'crud',
      'none': ''
    }
  }

  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('crud.resource'))

  def standardizeProperties(self):
    Structure = self.Structure
    Data = self.__Data__
    if isinstance(Structure['permissions'], basestring):
      Structure['permissions'] = Data['permissions'].get(Structure['permissions'], Structure['permissions'])

    for name, Prop in Structure.get('props', {}).iteritems():
      if not isMap(Prop):
        Structure['props'][name] = {'value': Prop}

@define('crud.field')
class field(node):
  r"""A class to process structures of type, crud.field.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('crud.field'))
