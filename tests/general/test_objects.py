# -*- coding: utf-8 -*-

from pyaction.general.objects import json_to_dict, dict_to_json
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

    def test_dict_to_json(self):
        test_dict = {"key1": "value1", "key2": "value2"}
        file_name = 'example_json_2.json'
        dict_to_json(os.path.join(files, file_name), data=test_dict)
        self.assertIn(file_name, os.listdir(files))

#-----------------------------------------------------------------------------
