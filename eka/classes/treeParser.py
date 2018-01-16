"""
The master class for other property parsers to depend upon.
"""
from eka.helpers import merge

class treeParser(object):
  def __init__(self, Config):
    self.__config__ = Config
    self.__addDefaultProperties__()

  def getConfig(self):
    return self.__config__

  def __addDefaultProperties__(self):
    r"""This method could be overridden by the child classes.
    """
    pass

  def processImports(self):
    Config = self.__config__
    Imports = Config.get('imports')

    print Config

    if Imports:
      Declarations = Config.setdefault('declarations')

      for _import in Imports:
        print _import

  def __parseStructure__(self):
    r"""This method could be overridden by the child classes.
    """
    pass
