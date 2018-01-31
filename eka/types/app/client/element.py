r"""
A class to process structures of type, app.client.element.
"""

from eka.classes.node import node

class element(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('fields'))
