r"""
Tests the type, app.server.
"""
from tests.helpers import BaseTestCase

from eka.classes.ymlParser import ymlParser
from eka.types.app import app
from eka.types.app.server import server
from eka.helpers import merge

# State
Buffer = {}

class TestTypeAppServer(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = app(ymlParser('master.yml').getConfig()['structure']['calculator']).getConfig()
    Buffer['server'] = Buffer['Config']['components']['server']

  def test_initialization(self):
    Parsed = server(Buffer['server']).getConfig()

    self.assertEquals(type(Parsed), dict)

if __name__ == '__main__':
  unittest.main()
