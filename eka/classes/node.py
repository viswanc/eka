r"""
The base class for other property parsers to depend upon.
"""

from eka.helpers import merge
from eka.helpers import getClassForType

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
    self.__standardizeProperties__()

    Providers = Structure.get('providers')

    if Providers:
      merge(Structure, *getProviders(Scopes, Providers if not isinstance(Providers, list) else [Providers]))

  def __standardizeProperties__(self):
    r"""This could be overrode by the child classes.
    """
    pass

  def __processBranches__(self, Branches, branchType=None):
    for Branch in (Branches or {}).values():
      if branchType and 'type' not in Branch:
        Branch['type'] = branchType

      if 'type' in Branch:
        Branch.update(getClassForType(Branch['type'])(self.Scopes, Branch).getStructure())

  def getStructure(self):
    return self.Structure
