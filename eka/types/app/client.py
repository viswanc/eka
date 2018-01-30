r"""
A class to process structures of type, app.client.
"""

from eka.classes.node import node

class client(node):
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure, 'elements')
