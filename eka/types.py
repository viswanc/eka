r"""
The root of all types.
"""

from eka.classes.node import node
from eka.helpers import isMap

# State
__Types__ = {}

# Helpers
def assign(typeName, Type):
  Type.__type__ = typeName
  __Types__[typeName] = Type

def define(typeName):
  return lambda Type: assign(typeName, Type)

# Exports
def getType(typeName):
  return __Types__.get(typeName)

# Types
@define('app')
class app(node):
  r"""A class to process structures of type, app.
  """
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('components'))

@define('app.client')
class client(node):
  r"""A class to process structures of type, app.client.
  """
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('elements'), 'app.client.element')

@define('app.client.element')
class element(node):
  r"""A class to process structures of type, app.client.element.
  """
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('fields'))

@define('app.server')
class server(node):
  r"""A class to process structures of type, app.server.
  """
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('resources'), 'app.server.resource')

@define('app.server.resource')
class resource(node):
  r"""A class to process structures of type, app.server.resource.
  """
  def __init__(self, Scopes, Structure):
    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('fields'), 'app.server.resource.field')

@define('app.server.resource.field')
class field(node):
  r"""A class to process structures of type, app.server.resource.field.
  """
  def __init__(self, Scopes, Structure):
    if not isMap(Structure):
      Structure = {'value': Structure}

    node.__init__(self, Scopes, Structure)
    self.__processBranches__(Structure.get('fields'), 'app.server.resource.field')
