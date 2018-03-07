r"""
The root of all plugin classes.
"""
from eka.classes.ymlParser import parseYML

# State
__Plugins__ = {}

# Helpers
def assign(className, Type):
  Type.__DefaultProperties__ = DP = getattr(Type, '__DefaultProperties__', {})
  DP['type'] = className
  __Plugins__[className] = Type

def loadPlugin(className):
  Plugins[className].load()

# Exports
def define(className):
  return lambda ClassDef: assign(className, ClassDef)

def getPluginClass(className):
  if className not in __Plugins__:
    loadPlugin(className) # #Note: __Plugins__ is populated by the module, loaded.

  return __Plugins__[className]

# Late Imports
from eka.classes.node import node

# Classes
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
          Component['buildBase'] = '.build/%s/%s' % (appName, componentName)

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

# Late imports
from eka.core.data import Plugins
