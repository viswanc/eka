"""
Eka - Core.
"""
from os import path

from eka import state
from eka.helpers import debug
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
    targetPath += '/treeParser.yml'

  else:
    if not path.isfile(targetPath):
      raise Exception('File not found: %s' % targetPath)

  base, filePath = path.split(targetPath)

  state.projectRoot = base

  return debug(treeParser(filePath, '').getConfig())

def getExternalModulePath(moduleString):
  return externalModulesRoot + moduleString.replace('.', '/')
