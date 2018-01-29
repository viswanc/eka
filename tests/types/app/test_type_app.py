r"""
Tests the type, app.
"""
from tests.helpers import BaseTestCase
from tests.data import TestData

from eka.classes.ymlParser import ymlParser
from eka.types.app import app
from eka.helpers import merge

# State
Buffer = {}
masterFile = '%s/master.yml' % TestData['projectRoot']

class TestTypeApp(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = ymlParser(masterFile).getConfig()
    Buffer['app'] = Buffer['Config']['structure']['calculator']

  def test_initialization(self):
    Parsed = app(masterFile).getConfig()

    self.assertEquals(type(Parsed), dict)
    self.assertIn('components', Parsed['structure']['calculator'])


if __name__ == '__main__':
  unittest.main()
