r"""
Tests the type, app.client.
"""
from tests.helpers import BaseTestCase
from tests.data import TestData

from eka.types.app import app
from eka.types.app.client import client
from eka.helpers import merge

# State
Buffer = {}
masterFile = '%s/master.yml' % TestData['projectRoot']

class TestTypeAppClient(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = app(masterFile).getConfig()['structure']['calculator']
    Buffer['client'] = Buffer['Config']['components']['client']

  def test_initialization(self):
    Parsed = client(masterFile).getConfig()

    self.assertEquals(type(Parsed), dict)

if __name__ == '__main__':
  unittest.main()
