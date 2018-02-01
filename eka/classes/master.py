r"""
The master class for other property parsers to depend upon.
"""

from eka.classes.node import node

class master(node):
  __DefaultProperties__ = {'type': 'master'}

  def __init__(self, Config):
    node.__init__(self, Config['Scopes'], Config['structure'])
    self.__processBranches__(Config['structure'].get('apps'), 'app')

  def __standardizeProperties__(self):
    for appName, App in self.Structure.get('apps', {}).iteritems():
      for componentName, Component in App.get('components', {}).iteritems():
        if not 'buildBase' in Component:
          Component['buildBase'] = '%s/%s' % (appName, componentName)
