r"""
Test helpers.
"""
import unittest

from eka import state

class BaseTestCase(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.__projectPathBuffer__ = state.projectRoot
    state.projectRoot = 'examples/mvp'

  @classmethod
  def tearDownClass(self):
    state.projectRoot = self.__projectPathBuffer__
