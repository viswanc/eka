r"""
A builder based on Jinja2 Templates.
"""
from jinja2 import Template

class jinjaBuilder(object):
  def __init__(self):
    pass

  def build(self, templateText, Data):
    return Template(templateText).render(Data)
