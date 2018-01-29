r"""
Tests the class, master.
"""
from tests.helpers import BaseTestCase
from tests.data import TestData

from eka.classes.ymlParser import ymlParser
from eka.classes.master import master

# State
Buffer = {}
masterFile = '%s/master.yml' % TestData['projectRoot']

class TestClassMaster(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = ymlParser(masterFile).getConfig()

  def test_initialization(self):
    Parsed = master(masterFile).getConfig()

    self.assertEquals(type(Parsed), dict)
    self.assertIn('structure', Parsed)

if __name__ == '__main__':
  unittest.main()
