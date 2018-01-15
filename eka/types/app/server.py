"""
A class to process structures of type, app.server.
"""

from eka.classes.treeParser import treeParser

class server(treeParser):
  def __init__(self, Config):
    treeParser.__init__(self, Config)
