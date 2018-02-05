r"""
The master builder.
"""
from os import mkdir
from os.path import abspath, dirname, exists
from importlib import import_module

from eka import state
from eka.classes.ymlParser import ymlParser
from eka.helpers import readFile, writeFile

# Data
builderDir = abspath(dirname(__file__) + '/../builders')

# Helpers
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
    builderName = Component.get('builder')

    if not builderName:
      return

    builderBase = '%s/%s' % (builderDir, builderName)
    configFile = '%s/config.yml' % builderBase

    if not exists(configFile):
      return

    Config = ymlParser(configFile).getConfig()
    Builder = resolveBuilder(Config['type'])
    builtSource = Builder.build(readFile('%s/%s' % (builderBase, Config['base'])), Component)

    buildTarget = '%s/.build/%s' % (state.projectRoot, Component['buildBase'])
    srcDir = '%s/src' % buildTarget

    from shutil import copytree, rmtree

    if exists(buildTarget):
      rmtree(buildTarget)
    copytree('%s/res' % builderBase, buildTarget)
    mkdir(srcDir)

    writeFile('%s/main.py' % srcDir, builtSource)
