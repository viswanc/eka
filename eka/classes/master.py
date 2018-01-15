"""
A class to import config from YAML files.
"""
from eka.helpers import getClassForType
from eka.classes.treeParser import treeParser

class master(treeParser):
  def __init__(self, Config):
    treeParser.__init__(self, Config)

  def __parseStructure__(self):
    Structure = self.__config__.get('structure')

    if Structure:
      for k, Config in Structure.iteritems():
        Structure[k].update(getClassForType(Config['type'])(Config).getConfig())
