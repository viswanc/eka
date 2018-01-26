"""
A class to import config from YAML files.
"""
import io
import yaml

class ymlParser(object):
  def __init__(self, filePath):
    self.__filePath__ = filePath
    self.__config__ = yaml.safe_load(io.open(self.__filePath__, 'r', encoding='utf8')) or {}

  def getConfig(self):
    return self.__config__
