r"""
Eka - Core.
"""
from os.path import dirname, isdir, isfile

from eka import state
from eka.helpers import debug
from eka.plugins import getPluginClass
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

  return treeParser(targetPath, '.').getConfig()

# Commands
def parse(targetPath, silent=False):
  Config = load(targetPath)
  Master = getPluginClass('master')(Config['structure'], Config['Scopes'])

  if not silent:
    print ymlParser().getDump(Master.Structure)

  return Master

def build(targetPath):
  parse(targetPath, True).build()

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
