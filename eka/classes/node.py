r"""
The base class for other property parsers to depend upon.
"""

from eka.classes.builder import Builder
from eka.classes.jsonSchemaExtender import ExtendedDraft4Validator
from eka.classes.ymlParser import parseYML
from eka.helpers import merge

def resolve(Scopes, providerName): # #pylint: disable=R1710
  for Scope in Scopes:
    if providerName in Scope:
      return Scope[providerName]

def getProviders(Scopes, Providers):
  return [val for val in [resolve(Scopes, provider) for provider in Providers] if val is not None]

# Exports
class node(object):
  __schema__ = parseYML(
  r"""
  $id: eka-v1 # http://example.com/eka-v1.json
  $schema: http://json-schema.org/draft-04/schema#
  description: The master schema for Eka documents.
  type: object

  definitions:
    providable:
      providers:
        type: [string, array]

    expression: {}

  properties: {}
  """)

  def __init__(self, Structure, Scopes=None, SchemaExtensions=None):
    self.Structure = Structure
    self.Scopes = Scopes
    self.Props = {}
    self.standardizeProperties()

    if not hasattr(Structure, 'iteritems'):
      return

    Providers = Structure.get('providers')

    if Scopes and Providers:
      merge(Structure, *getProviders(Scopes, Providers if isinstance(Providers, list) else [Providers]))

    if SchemaExtensions:
      self.__schema__ = merge({}, self.__schema__, SchemaExtensions)

    self.parse()

    PropStructures = self.Structure.get('props', {})
    Props = self.Props

    for name, PropStructure in PropStructures.iteritems():
      Prop = getPluginClass(PropStructure['class'])(PropStructure, self.Scopes)
      Props[name] = Prop
      PropStructures[name] = Prop.Structure

  def standardizeProperties(self):
    pass

  def parse(self):
    ExtendedDraft4Validator(self.__schema__).validate(self.Structure)

  def build(self):
    for Prop in self.Props.values():
      Builder(Prop).build()

# Late Imports
from eka.plugins import getPluginClass
