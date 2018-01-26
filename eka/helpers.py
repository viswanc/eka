"""
Helpers
"""
from sys import stderr
from importlib import import_module

from eka import state

# Exports
def getClassForType(type):
  return getattr(import_module('.types.' + type, package='eka'), type[type.rfind('.') + 1:])

def merge(*Dicts):
  Ret = {}

  for Dict in Dicts:
    for k, v in Dict.iteritems():
      target = Ret.get(k)

      if hasattr(target, 'iteritems') and hasattr(v, 'iteritems'):
        Ret[k] = merge(target, v)
      else:
        Ret[k] = v

  return Ret

def debug(something):
  if state.debug:
    stderr.write(unicode(something) + u'\n')

  return something
