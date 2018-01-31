r"""
Tests the class, ymlParser.
"""
import unittest
from tests.helpers import BaseTestCase
from tests.data import TestData

from eka.classes.ymlParser import ymlParser

# Data
masterFile = '%s/master.yml' % TestData['projectRoot']

class TestYmlParser(BaseTestCase):
  def test_config_loading_from_file(self):
    r"""
    When a file path is given, the config should be loaded from the file.
    """
    self.assertEquals(type(ymlParser(masterFile).getConfig()), dict)

if __name__ == '__main__':
  unittest.main()
