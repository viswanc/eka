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
  def __init__(self, Scopes, Structure, branchProperty=None):
    self.Structure = Structure
    Branches = (Structure[branchProperty] if branchProperty else Structure)

    for name, Branch in Branches.iteritems():
      Branches[name] = self.processBranch(Branch, Scopes)

  def processBranch(self, Branch, Scopes):
    Providers = Branch.get('providers')

    if Providers:
      Branch = merge(Branch, *getProviders(Scopes, [Providers] if type(Providers) != list else Providers))

    if 'type' in Branch:
      Branch.update(getClassForType(Branch['type'])(Scopes, Branch).getStructure())

    return Branch

  def getStructure(self):
    return self.Structure
