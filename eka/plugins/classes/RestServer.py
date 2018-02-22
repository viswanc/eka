r"""
The plugin class, rest.server.
"""
from eka.classes.node import node
from eka.classes.ymlParser import parseYML
from eka.helpers import isMap
from eka.core.plugin_classes import define

# Data
Definitions = parseYML(r"""
  rest.server:
    allOf:
      - $ref: '#/definitions/providable'
      - type: object
        properties:
          class:
            enum: [rest.server]
            default: rest.server
          builder:
            type: string
          buildBase:
            type: string
          props:
            type: object
            patternProperties:
              '^([A-z0-9_-])+$':
                $ref: '#/definitions/rest.server.resource'

  rest.server.resource:
    allOf:
      - $ref: '#/definitions/providable'
      - type: object
        properties:
          class:
            enum: [rest.server.resource]
            default: rest.server.resource
          permissions:
            type: string
            default: crud
            pattern: '^[crud]+|all|none|$'
          props:
            type: object
            patternProperties:
              '^([A-z0-9_-])+$':
                $ref: '#/definitions/rest.server.resource.field'

  rest.server.resource.field:
      allOf:
        - $ref: '#/definitions/providable'
        - anyOf:
          - type: [integer, string]
          - type: object
            properties:
                class:
                  enum: [rest.server.resource.field]
                  default: rest.server.resource.field
                value:
                  type: [integer, string]
""")

# Helpers
def getSchemaExtension(className):
  Schema = {'definitions': Definitions}
  Schema.update(Definitions[className])

  return Schema

@define('rest.server')
class server(node):
  r"""A class to process structures of type, rest.server.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('rest.server'))

@define('rest.server.resource')
class resource(node):
  r"""A class to process structures of type, rest.server.resource.
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
    node.__init__(self, Structure, Scopes, getSchemaExtension('rest.server.resource'))

  def standardizeProperties(self):
    Structure = self.Structure
    Data = self.__Data__
    if isinstance(Structure['permissions'], basestring):
      Structure['permissions'] = Data['permissions'].get(Structure['permissions'], Structure['permissions'])

    for name, Prop in Structure.get('props', {}).iteritems():
      if not isMap(Prop):
        Structure['props'][name] = {'value': Prop}

@define('rest.server.resource.field')
class field(node):
  r"""A class to process structures of type, rest.server.resource.field.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('rest.server.resource.field'))
