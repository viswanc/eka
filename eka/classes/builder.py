r"""
The master builder.
"""

from os import rename, makedirs
from os.path import dirname, exists
from importlib import import_module

from eka import state

# Helpers
def loadBuilder(builderName):
  import pkg_resources

  prefix = 'eka.plugins.builders'
  return pkg_resources.load_entry_point('%s.%s' % (prefix, builderName), prefix, builderName)

def resolveBuilder(builderType):
  return getattr(import_module('eka.classes.builders.' + builderType), builderType + 'Builder')()

class Builder(object):
  def __init__(self, Structure):
    self.Structure = Structure

  def build(self):
    for App in self.Structure['props'].values():
      for Component in App['props'].values():
        self.buildComponent(Component)

  def buildComponent(self, Component):
    builderName = Component.get('builder') # #ToDo: Use class based builders, instead.

    if not builderName:
      return

    Builder = loadBuilder(builderName)
    builtDir = Builder.build(Component)
    targetDir = '%s/.build/%s' % (state.projectRoot, Component['buildBase'])
    targetParent = dirname(targetDir)

    if not exists(targetParent):
      makedirs(targetParent)

    elif exists(targetDir):
      from shutil import rmtree
      rmtree(targetDir)

    rename(builtDir, targetDir) # #ToDo: Fix: This might not work across volumes.
