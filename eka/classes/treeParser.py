"""
The master class for other property parsers to depend upon.
"""
from os.path import dirname, exists

from eka.helpers import debug, merge
from eka import state
from eka.state import Modules
from eka.classes.ymlParser import ymlParser

class treeParser(object):
  def __init__(self, filePath, namespace='.'):
    debug('importing: %s as %s' % (filePath, namespace))

    self.__config__ = Modules[namespace] = ymlParser(filePath).getConfig()
    self.__config__.setdefault('Scopes', [{}])
    self.__moduleDir__ = dirname(filePath)
    self.__namespace__ = namespace
    self.__processImports__()

  def getConfig(self):
    return self.__config__

  def __loadImport__(self, moduleString):
    modulePath = moduleString.replace('.', '/') + '.yml'

    if moduleString[0] == '.': # An initial dot says that the module is a descendant of the projectRoot.
      moduleNamespace = moduleString
      modulePath = state.projectRoot + modulePath

    else:
      modulePath = '%s/%s' % (self.__moduleDir__, modulePath)

      if exists(modulePath):
        moduleNamespace = '%s.%s' % (self.__namespace__[:self.__namespace__.rfind('.')], moduleString) # This is a relative import.

      else: # This import is from an external package.
        moduleNamespace = moduleString
        modulePath = '%s%s.yml' % (state.externalModulesRoot, moduleNamespace.replace('.', '/'))

    if moduleNamespace in Modules:
      return Modules[moduleNamespace]

    return treeParser(modulePath, moduleNamespace).getConfig()

  def __processImports__(self):
    Config = self.__config__

    for importExpression in Config.get('imports') or []:
      if not importExpression:
        raise Exception('Module string not provided for import')

      Expressions = importExpression.split(' ') # #Pending: Use regex to allow for multiple spaces, may be with a function, normalize.
      moduleString = Expressions[0]
      importChildren = moduleString[-2:] == '.*'
      expressionCount = len(Expressions)

      if expressionCount > 1 and (importChildren or expressionCount != 3 or Expressions[1] != 'as'):
        raise Exception('Invalid import expression: %s' % importExpression)

      if importChildren:
        moduleString = moduleString[:-2]

      Imported = self.__loadImport__(moduleString)

      if 'imports' in Config:
        del Config['imports']

      if 'structure' in Imported:
        GlobalScope = Config['Scopes'][0]

        if importChildren:
          Config['Scopes'][0] = merge(GlobalScope, Imported['structure'])

        else:
          moduleName = Expressions[2] if expressionCount > 1 else moduleString[moduleString.rfind('.') + 1:]
          GlobalScope[moduleName] = Imported['structure']

  def __processAliases__(self):
    pass

  def __parseStructure__(self):
    pass
