r"""
Test helpers.
"""
from tests.data import TestData

import unittest

from eka import state

class BaseTestCase(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.__projectPathBuffer__ = state.projectRoot
    state.projectRoot = TestData['projectRoot']

  @classmethod
  def tearDownClass(self):
    state.projectRoot = self.__projectPathBuffer__
