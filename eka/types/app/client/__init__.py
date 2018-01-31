r"""
A class to process structures of type, app.client.
"""

from eka.classes.node import node

class client(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure, Structure.get('elements'))

  def __addDefaultProperties__(self):
    for Branch in self.Structure.get('elements', {}).values():
      Branch['type'] = 'app.client.element'
