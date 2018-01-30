r"""
The master class for other property parsers to depend upon.
"""

from eka.classes.node import node

class master(node):
  def __init__(self, Config):
    node.__init__(self, Config['Scopes'], Config['structure'])
