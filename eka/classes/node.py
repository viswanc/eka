r"""
The base class for other property parsers to depend upon.
"""
from eka.helpers import merge

def resolve(Scopes, providerName): # #pylint: disable=R1710
  for Scope in Scopes:
    if providerName in Scope:
      return Scope[providerName]

def getProviders(Scopes, Providers):
  return [val for val in [resolve(Scopes, provider) for provider in Providers] if val is not None]

class node(object):
  def __init__(self, Scopes, Structure):
    self.Structure = Structure
    self.Scopes = Scopes
    self.__addDefaultProperties__()
    self.__standardizeProperties__()

    Providers = Structure.get('providers')

    if Providers:
      merge(Structure, *getProviders(Scopes, Providers if isinstance(Providers, list) else [Providers]))
      del Structure['providers']

  def __addDefaultProperties__(self):
    r"""
    """
    if not 'type' in self.Structure:
      self.Structure['type'] = self.__type__

  def __standardizeProperties__(self):
    r"""This could be overrode by the child classes.
    """
    pass

  def __processBranches__(self, Branches, defaultBranchType=None):
    for name, Branch in (Branches or {}).iteritems():
      Branches[name] = getType(defaultBranchType or Branch['type'])(self.Scopes, Branch).getStructure()

  def getStructure(self):
    return self.Structure

# Late imports
from eka.types import getType
