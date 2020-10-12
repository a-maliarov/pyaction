# -*- coding: utf-8 -*-

from pyaction.general.objects import json_to_dict
import unittest
import sys
import os

#-----------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))
files = os.path.join(here, 'files')

class TestGeneralObjects(unittest.TestCase):

    def test_json_to_dict(self):
        data = json_to_dict(os.path.join(files, 'example_json.json'))
        self.assertEqual(data, {"key1": "value1", "key2": "value2"})

#-----------------------------------------------------------------------------
