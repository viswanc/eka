"""
A class to process structures of type, app.client.
"""

from eka.classes.treeParser import treeParser

class client(treeParser):
  def __init__(self, Config):
    treeParser.__init__(self, Config)
