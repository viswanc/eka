r"""
The master builder.
"""
from os import mkdir
from os.path import abspath, dirname, exists
from importlib import import_module

from eka import state
from eka.classes.ymlParser import ymlParser
from eka.helpers import readFile, writeFile

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
    builderName = Component.get('builder') # #ToDo: Fix the builder logic.

    if not builderName:
      return

    builderDir = dirname(loadBuilder(builderName).__file__)

    configFile = '%s/config.yml' % builderDir

    if not exists(configFile):
      return

    Config = ymlParser(configFile).getConfig()
    Builder = resolveBuilder(Config['type'])
    builtSource = Builder.build(readFile('%s/%s' % (builderDir, Config['base'])), Component)

    buildTarget = '%s/.build/%s' % (state.projectRoot, Component['buildBase'])
    srcDir = '%s/src' % buildTarget

    from shutil import copytree, rmtree

    if exists(buildTarget):
      rmtree(buildTarget)
    copytree('%s/res' % builderDir, buildTarget)
    mkdir(srcDir)

    writeFile('%s/main.py' % srcDir, builtSource)
