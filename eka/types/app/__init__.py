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
    Components = self.__config__['components']

    for k, Config in Components.iteritems():
      Components[k] = merge(Config, getClassForType(Config['type'])(ymlParser(Config['path']).getConfig()).getConfig())
