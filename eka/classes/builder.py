r"""
The master builder.
"""

from os import rename

from laufire.filesys import ensureParent, removePath
from eka import state

class Builder(object):
  def __init__(self, Node):
    self.Node = Node

  def build(self):
    builtDir = self.Node.build()

    if not builtDir:
      return

    targetDir = '%s/.build/%s' % (state.projectRoot, self.Node.Structure['buildBase'])
    ensureParent(targetDir)
    removePath(targetDir)

    rename(builtDir, targetDir) # #ToDo: Fix: This might not work across volumes.
