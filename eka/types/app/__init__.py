"""
A class to process structures of type, app.
"""

from eka.helpers import getClassForType, merge
from eka.classes.treeParser import treeParser
from eka.classes.ymlParser import ymlParser

class app(treeParser):
  def __init__(self, Config):
    treeParser.__init__(self, Config)

  def __addDefaultProperties__(self):
    namespace = self.__config__['namespace']

    for k, Config in self.__config__['components'].iteritems():
      Config.setdefault('path', '%s.yml' % k)
      Config['namespace'] = namespace + '.' + Config.get('namespace', k)

  def __parseStructure__(self):
    ComponentConfigs = self.__config__['components']
    Components = {}

    for k, Config in ComponentConfigs.iteritems():
      Component = getClassForType(Config['type'])(ymlParser(Config['path'])
      Components[k] = Component
      ComponentConfigs[k] = merge(Config, Component.getConfig()).getConfig())

    for k, Component in Components.iteritems():
      Component.
