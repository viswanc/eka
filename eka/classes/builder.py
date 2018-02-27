r"""
The master builder.
"""

from os import rename, makedirs
from os.path import dirname, exists

from eka import state

class Builder(object):
  def __init__(self, Node):
    self.Node = Node

  def build(self):
    builtDir = self.Node.build()

    if not builtDir:
      return

    targetDir = '%s/.build/%s' % (state.projectRoot, self.Node.Structure['buildBase'])
    targetParent = dirname(targetDir)

    if not exists(targetParent):
      makedirs(targetParent)

    elif exists(targetDir):
      from shutil import rmtree
      rmtree(targetDir)

    rename(builtDir, targetDir) # #ToDo: Fix: This might not work across volumes.
