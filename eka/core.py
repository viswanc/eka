r"""
Eka - Core.
"""
from os.path import abspath, dirname, isdir, isfile

from eka import state
from eka.helpers import debug
from eka.classes.master import master
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
  return debug(master(treeParser(targetPath, '.').getConfig()).getStructure(), True)

def validateStructure(Data):
  from jsonschema import validate

  validate(Data, ymlParser('%s/data/masterSchema.yml' % dirname(abspath(__file__))).getConfig())

def build(targetPath):
  from eka.classes.builder import Builder

  print ymlParser().getDump(load(targetPath))

  Builder(load(targetPath)).build()

# Exports
def init(Argv):
  target_path = Argv.pop(0)

  if '--debug' in Argv:
    state.debug = True

  if target_path:
    build(target_path)
