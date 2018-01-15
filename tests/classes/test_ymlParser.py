r"""
Tests the class, ymlParser.
"""
from tests.helpers import BaseTestCase

from eka.classes.ymlParser import ymlParser

# Data
mvpPath = 'master.yml'

class TestYmlParser(BaseTestCase):
  def test_config_loading_from_file(self):
    r"""
    When a file path is given, the config should be loaded from the file.
    """
    self.assertEquals(type(ymlParser(mvpPath).getConfig()), dict)

if __name__ == '__main__':
  unittest.main()
