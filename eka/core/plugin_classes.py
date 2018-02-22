r"""
The root of all plugin classes.
"""
import pkg_resources
from eka.classes.ymlParser import parseYML

# State
__Classes__ = {}

# Helpers
def assign(typeName, Type):
  Type.__DefaultProperties__ = DP = getattr(Type, '__DefaultProperties__', {})
  DP['type'] = typeName
  __Classes__[typeName] = Type

def loadClass(className):
  return pkg_resources.load_entry_point('eka', 'eka.plugins.classes', className)

# Exports
def define(typeName):
  return lambda Type: assign(typeName, Type)

def getPluginClass(typeName):
  if typeName not in __Classes__:
    loadClass(typeName)

  return __Classes__.get(typeName)

# Late Imports
from eka.classes.node import node

# Types
@define('master')
class master(node):
  r"""A class to process structures of type, master.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, parseYML(u"""
    properties:
      props:
        type: object
        patternProperties:
          '^([A-z0-9_-])+$': {}
      class:
        enum: [master]
        default: master
    """))

  def standardizeProperties(self):
    for appName, App in self.Structure.get('props', {}).iteritems():
      for componentName, Component in App.get('props', {}).iteritems():
        if not 'buildBase' in Component:
          Component['buildBase'] = '%s/%s' % (appName, componentName)

@define('rest.app')
class app(node):
  r"""A class to process structures of type, app.
  """
  def __init__(self, Structure, Scopes):
    node.__init__(self, Structure, Scopes, parseYML(u"""
    properties:
      allOf:
        - $ref: '#/definitions/providable'
        - type: object
          properties:
            class:
              enum: [app]
              default: app
            props:
              type: object
              patternProperties:
                '^([A-z0-9_-])+$': {}
    """))
