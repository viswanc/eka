r"""
A class to process structures of type, app.server.
"""

from eka.classes.node import node

class server(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure, Structure.get('resources'))

  def __addDefaultProperties__(self):
    for Branch in self.Structure.get('resources', {}).values():
      Branch['type'] = 'app.server.resource'
