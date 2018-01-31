r"""
A class to process structures of type, app.server.
"""

from eka.classes.node import node

class server(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('resources'), 'app.server.resource')
