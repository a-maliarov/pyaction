# -*- coding: utf-8 -*-

from pyaction.multiprocessing_.objects import *
import unittest
import sys
import os

#-----------------------------------------------------------------------------

class TestMultiprocessingObjects(unittest.TestCase):

    def test_chunk(self):
        input_list = [1, 2, 3, 4, 5, 6]
        parts = 4
        output_list = chunk(input_list, parts)
        self.assertEqual(output_list, [[1, 2], [3, 4], [5], [6]])

#-----------------------------------------------------------------------------
