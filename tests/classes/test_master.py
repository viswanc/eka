r"""
Tests the class, master.
"""
from tests.helpers import BaseTestCase

from eka.classes.ymlParser import ymlParser
from eka.classes.master import master

# State
Buffer = {}

class TestClassMaster(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = ymlParser('master.yml').getConfig()

  def test_initialization(self):
    Parsed = master(Buffer['Config']).getConfig()

    self.assertEquals(type(Parsed), dict)
    self.assertIn('structure', Parsed)

if __name__ == '__main__':
  unittest.main()
