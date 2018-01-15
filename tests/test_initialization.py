r"""
Tests the intialization.
"""
import unittest

from eka import core

# Data
mvpPath = 'examples/mvp'

class TestInitialization(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_raise_exception_on_missing_file(self):
    r"""
    An exception should be risen, when the config file is missing.
    """
    with self.assertRaises(Exception) as context:
      core.load('%s/master.gibberish' % mvpPath)

    self.assertTrue('not found' in str(context.exception))

  def test_config_loading_from_file(self):
    r"""
    When a file path is given, the config should be loaded from the file.
    """
    self.assertEquals(type(core.load('%s/master.yml' % mvpPath)), dict)

  def test_config_loading_from_dir(self):
    r"""
    When a dir is given, config should be loaded from master.yml under the dir.
    """
    self.assertEquals(cmp(core.load('%s/master.yml' % mvpPath), core.load(mvpPath)), 0)

if __name__ == '__main__':
  unittest.main()
