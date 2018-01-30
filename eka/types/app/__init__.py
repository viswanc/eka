r"""
A class to process structures of type, app.
"""

from eka.classes.node import node

class app(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure, 'components')
