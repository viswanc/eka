r"""
The base class for other property parsers to depend upon.
"""
from os.path import dirname, exists

from eka.helpers import merge
from eka.helpers import getClassForType

def resolve(Scopes, providerName):
  for Scope in Scopes:
    if providerName in Scope:
      return Scope[providerName]

def getProviders(Scopes, Providers):
  return filter(lambda val: val is not None, [resolve(Scopes, provider) for provider in Providers])

class node(object):
  def __init__(self, Scopes, Structure, Branches=None):
    self.Structure = Structure
    self.__addDefaultProperties__()

    for name, Branch in (Branches or {}).iteritems():
      Branches[name] = self.__processBranch__(Branch, Scopes)

  def __addDefaultProperties__(self):
    r"""This could be overrode by the child classes.
    """
    pass

  def __processBranch__(self, Branch, Scopes):
    Providers = Branch.get('providers')

    if Providers:
      Branch = merge(Branch, *getProviders(Scopes, [Providers] if type(Providers) != list else Providers))

    if 'type' in Branch:
      Branch.update(getClassForType(Branch['type'])(Scopes, Branch).getStructure())

    return Branch

  def getStructure(self):
    return self.Structure
