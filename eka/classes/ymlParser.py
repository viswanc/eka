"""
A class to import config from YAML files.
"""
import yaml

from eka import state

class ymlParser(object):
  def __init__(self, filePath):
    self.__filePath__ = filePath
    self.__config__ = yaml.safe_load(open('%s/%s' % (state.projectRoot, self.__filePath__), 'r')) or {}

  def getConfig(self):
    return self.__config__
