r"""
Eka - Core.
"""
from os.path import dirname, isdir, isfile

from eka import state
from eka.helpers import debug
from eka.core.plugin_classes import getPluginClass
from eka.classes.treeParser import treeParser
from eka.classes.ymlParser import ymlParser

# Helpers
def getExternalModulePath(moduleString):
  return state.externalModulesRoot + moduleString.replace('.', '/')

def load(targetPath):
  if isdir(targetPath):
    targetPath += '/master.yml'

  else:
    if not isfile(targetPath):
      raise Exception('File not found: %s' % targetPath)

  state.projectRoot = dirname(targetPath)
  Config = treeParser(targetPath, '.').getConfig()
  return debug(getPluginClass('master')(Config['structure'], Config['Scopes']).Structure, True)

# Commands
def parse(targetPath, silent=False):
  Data = load(targetPath)

  if not silent:
    print ymlParser().getDump(Data)

  return Data

def build(targetPath):
  from eka.classes.builder import Builder
  Builder(parse(targetPath, True)).build()

# Exports
def init(Argv):
  command = Argv[0]
  targetPath = Argv[1]

  if '--debug' in Argv:
    state.debug = True

  if command == 'build':
    build(targetPath)

  elif command == 'parse':
    parse(targetPath)
