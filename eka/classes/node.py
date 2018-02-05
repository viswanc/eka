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
    self.__standardizeProperties__()

    if not hasattr(Structure, 'iteritems'):
      return

    Providers = Structure.get('providers')

    if Providers:
      merge(Structure, *getProviders(Scopes, Providers if isinstance(Providers, list) else [Providers]))
      # del Structure['providers'] # #ToDo: Remove the providers. It isn't done as of now, as the master schema doesn't allow for missing providers.

    Props = self.Structure.get('props', {})

    for name, Prop in Props.iteritems():
      Props[name] = node(self.Scopes, Prop).getStructure()

  def __standardizeProperties__(self):
    r"""This could be overrode by the child classes.
    """
    pass

  def getStructure(self):
    return self.Structure
