"""
The master class for other property parsers to depend upon.
"""
class treeParser(object):
  def __init__(self, Config):
    self.__config__ = Config
    self.__parseStructure__()

  def getConfig(self):
    return self.__config__

  def __parseStructure__(self):
    r"""This method could be overridden by the child classes.
    """
    return
