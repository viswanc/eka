r"""
Tests the type, app.server.
"""
from tests.helpers import BaseTestCase
from tests.data import TestData

from eka.types.app import app
from eka.types.app.server import server
from eka.helpers import merge

# State
Buffer = {}
masterFile = '%s/master.yml' % TestData['projectRoot']

class TestTypeAppserver(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = app(masterFile).getConfig()['structure']['calculator']
    Buffer['server'] = Buffer['Config']['components']['server']

  def test_initialization(self):
    Parsed = server(masterFile).getConfig()

    self.assertEquals(type(Parsed), dict)

if __name__ == '__main__':
  unittest.main()
