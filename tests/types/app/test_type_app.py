r"""
Tests the type, app.
"""
from tests.helpers import BaseTestCase

from eka.classes.ymlParser import ymlParser
from eka.types.app import app
from eka.helpers import merge

# State
Buffer = {}

class TestTypeApp(BaseTestCase):
  @classmethod
  def setUpClass(self):
    BaseTestCase.setUpClass()
    Buffer['Config'] = ymlParser('master.yml').getConfig()
    Buffer['app'] = Buffer['Config']['structure']['calculator']

  def test_initialization(self):
    Parsed = app(Buffer['app']).getConfig()

    self.assertEquals(type(Parsed), dict)
    self.assertIn('components', Parsed)

  def test_path_property_default(self):
    ModifiedConfig = merge({}, Buffer['app'])
    del ModifiedConfig['components']['client']['path']

    ParsedFromModifiedConfig = app(ModifiedConfig).getConfig()
    ParsedFromOriginalConfig = app(Buffer['app']).getConfig()

    self.assertIn('path', ModifiedConfig['components']['client']) # The missing path property should've been filled.
    self.assertEquals(cmp(ParsedFromModifiedConfig, ParsedFromOriginalConfig), 0) # The built trees should be identical.

if __name__ == '__main__':
  unittest.main()
