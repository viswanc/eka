r"""
A class to import config from YAML files.
"""
import io
import yaml
from collections import OrderedDict

# Init
# YAML Ordered dicts loading and dumping.
# #From: https://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts/21048064
class OrderedLoader(yaml.SafeLoader):
  pass

def construct_mapping(loader, node):
  loader.flatten_mapping(node)
  return OrderedDict(loader.construct_pairs(node))

OrderedLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)

class OrderedDumper(yaml.SafeDumper):
  pass

def _dict_representer(dumper, data):
  return dumper.represent_mapping(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items())

OrderedDumper.add_representer(OrderedDict, _dict_representer)

# Exports
class ymlParser(object):
  def __init__(self, filePath=None):
    if filePath:
      self.__filePath__ = filePath
      self.__config__ = yaml.load(io.open(self.__filePath__, 'r', encoding='utf8'), OrderedLoader) or {}

  def getConfig(self):
    return self.__config__

  def getDump(self, Data=None):
    return yaml.dump(Data or self.__config__, None, OrderedDumper)
