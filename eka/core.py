r"""
Eka - Core.
"""
from os import path

from eka import state
from eka.helpers import debug
from eka.classes.master import master
from eka.classes.treeParser import treeParser

# Helpers
# None, yet.

# Exports
def init(Argv):
  target_path = Argv.pop(0)

  if '--debug' in Argv:
    state.debug = True

  if target_path:
    load(target_path)

def load(targetPath):
  if path.isdir(targetPath):
    targetPath += '/master.yml'

  else:
    if not path.isfile(targetPath):
      raise Exception('File not found: %s' % targetPath)

  state.projectRoot = path.dirname(targetPath)
  return debug(master(treeParser(targetPath, '.').getConfig()).getStructure(), True)

def getExternalModulePath(moduleString):
  return state.externalModulesRoot + moduleString.replace('.', '/')
