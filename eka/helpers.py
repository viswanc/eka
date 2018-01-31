r"""
Helpers
"""
from sys import stderr
from importlib import import_module

from eka import state

# Exports
def getClassForType(type):
  return getattr(import_module('.types.' + type, package='eka'), type[type.rfind('.') + 1:])

def merge(*Dicts):
  Base = Dicts[0] # #Note: The base dict gets altered.
  for Dict in Dicts[1:]:
    for k, v in Dict.iteritems():
      target = Base.get(k)

      if hasattr(target, 'iteritems') and hasattr(v, 'iteritems'):
        Base[k] = merge(target, v)
      else:
        Base[k] = v

  return Base

def debug(something, prettify=False):
  if state.debug:
    stderr.write(unicode(getYAMLDump(something) if prettify else something) + u'\n')

  return something

def getYAMLDump(Data):
  from eka.classes.ymlParser import ymlParser
  return ymlParser().getDump(Data)
