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

# def parse(targetPath):
#   from jsonschema import validate
#
#   Data = load(targetPath)
#   validate(Data, ymlParser('%s/data/masterSchema.yml' % dirname(abspath(__file__))).getConfig())
#   print ymlParser().getDump(load(targetPath))
#
#   return Data

def parse(targetPath):
  from eka.classes.jsonSchemaExtender import ExtendedDraft4Validator

  Data = load(targetPath)
  ExtendedDraft4Validator(ymlParser('%s/data/masterSchema.yml' % dirname(abspath(__file__))).getConfig()).validate(Data)
  print ymlParser().getDump(Data)
  return Data

def build(targetPath):
  from eka.classes.builder import Builder
  Builder(parse(targetPath)).build()

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
