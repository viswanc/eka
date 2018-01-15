r"""
Tests the type, app.client.
"""
from tests.helpers import BaseTestCase

from eka.classes.ymlParser import ymlParser
from eka.types.app import app
from eka.types.app.client import client
from eka.helpers import merge

# State
Buffer = {}

class TestTypeAppClient(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = app(ymlParser('master.yml').getConfig()['structure']['calculator']).getConfig()
    Buffer['client'] = Buffer['Config']['components']['client']

  def test_initialization(self):
    Parsed = client(Buffer['client']).getConfig()

    self.assertEquals(type(Parsed), dict)

if __name__ == '__main__':
  unittest.main()
