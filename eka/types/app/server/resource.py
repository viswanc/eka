r"""
A class to process structures of type, app.server.resource.
"""

from eka.classes.node import node

class resource(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('fields'))

  def __standardizeProperties__(self):
    Branches = self.Structure.get('fields', {})

    for name, Branch in Branches.iteritems():
      if not hasattr(Branch, 'iteritems'):
        Branches[name] = {'value': Branch}
