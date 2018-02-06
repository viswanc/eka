r"""
The master class for other property parsers to depend upon.
"""

from eka.classes.node import node

class master(node):
  def __init__(self, Config):
    node.__init__(self, Config['Scopes'], Config['structure'])

  def __standardizeProperties__(self):
    for appName, App in self.Structure.get('props', {}).iteritems():
      for componentName, Component in App.get('props', {}).iteritems():
        if not 'buildBase' in Component:
          Component['buildBase'] = '%s/%s' % (appName, componentName)
