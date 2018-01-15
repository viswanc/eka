r"""
Tests the intialization.
"""
import unittest

# Data
mvpPath = 'examples/mvp'

class TestInitialization(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_verify_config_loading_from_dir(self):
    from eka import core

    core.load(mvpPath)

  def test_verify_config_loading_from_file(self):
    from eka import core

    core.load('%s/master.yml' % mvpPath)

if __name__ == '__main__':
  unittest.main()
