r"""
A builder based on Jinja2 Templates.
"""

from laufire.filesys import copyContent, ensureCleanDir, ensureDir, getContent, getPathPairs, getPathType, setContent
from jinja2 import Template

class jinjaBuilder(object):
  def __init__(self):
    pass

  def render(self, templateText, Data):
    return Template(templateText).render(Data)

  def build(self, srcPath, tgtPath, Data):
    ensureCleanDir(tgtPath)

    for src, tgt in getPathPairs(srcPath, tgtPath):
      if getPathType(src) != 1:
        ensureDir(tgt)

      elif tgt[-6:] != '.jinja':
        copyContent(src, tgt)

      else:
        setContent(tgt[:-6], Template(getContent(src)).render(Data))

    return tgtPath
