r"""
A class to process structures of type, app.server.resource.
"""

from eka.classes.node import node

class resource(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure, Structure.get('fields'))

  def __addDefaultProperties__(self):
    Branches = self.Structure.get('fields', {})

    for name, Branch in Branches.iteritems():
      if not isinstance(Branch, dict):
        Branches[name] = {'value': Branch}
