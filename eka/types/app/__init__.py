"""
A class to process structures of type, app.
"""

from eka.helpers import getClassForType, merge
from eka.classes.ymlParser import ymlParser

class app:
  def __init__(self, Config):
    self.__config__ = Config

  def getConfig(self):
    Components = self.__config__['components']

    for k, Config in Components.iteritems():
      Config.setdefault('path', '%s.yml' % k) # #Note: Missing properties are added to the tree, by default
      Components[k] = merge(Components[k], getClassForType(Config['type'])(ymlParser(Config['path']).getConfig()).getConfig(), {})

    return self.__config__
