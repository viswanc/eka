r"""
A class to process structures of type, app.client.element.
"""

from eka.classes.node import node

class element(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure, Structure.get('fields'))
