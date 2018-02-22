r"""
The plugin class, rest.client.
"""
from eka.classes.node import node
from eka.classes.ymlParser import parseYML
from eka.core.plugin_classes import define

# Data
Definitions = parseYML(r"""
  rest.client: # #Note: Nested definitions (like app/client) aren't used, as it complicates the schema.
    allOf:
      - $ref: '#/definitions/providable'
      - type: object
        properties:
          class:
            enum: [rest.client]
            default: rest.client
          buildBase:
            type: string
          uiRoot:
            type: string
          props:
            type: object
            patternProperties:
              '^([A-z0-9_-])+$':
                $ref: '#/definitions/rest.client.element'

  rest.client.element:
      allOf:
        - $ref: '#/definitions/providable'
        - type: object
          properties:
            class:
              enum: [rest.client.element]
              default: rest.client.element
            value:
              type: string
            props:
              patternProperties:
                '^([A-z0-9_-])+$':
                  anyOf:
                    - $ref: '#/definitions/rest.client.element'
                    - $ref: '#/definitions/rest.client.element.button'

  rest.client.element.button:
    allOf:
      - $ref: '#/definitions/providable'
      - type: object
        properties:
          title:
            type: string
          action:
            type: string
          class:
            enum: [rest.client.element.button]
            default: rest.client.element.button
""")

# Helpers
def getSchemaExtension(className):
  Schema = {'definitions': Definitions}
  Schema.update(Definitions[className])

  return Schema

@define('rest.client')
class client(node):
  r"""A class to process structures of type, rest.client.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('rest.client'))

@define('rest.client.element')
class element(node):
  r"""A class to process structures of type, rest.client.element.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('rest.client.element'))

@define('rest.client.element.button')
class button(node):
  r"""A class to process structures of type, rest.client.element.button.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, getSchemaExtension('rest.client.element.button'))
