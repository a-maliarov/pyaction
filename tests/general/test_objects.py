# -*- coding: utf-8 -*-

from pyaction.general.objects import *
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
        file_path = os.path.join(files, file_name)
        dict_to_json(file_path, data=test_dict)
        result = file_name in os.listdir(files)
        os.remove(file_path)
        self.assertTrue(result)

    def test_file_to_list_with_duplicates(self):
        file_name = 'example_txt.txt'
        output = file_to_list(os.path.join(files, file_name))
        self.assertEqual(output, ['1', '1', '2', '3'])

    def test_file_to_list_without_duplicates(self):
        file_name = 'example_txt.txt'
        output = file_to_list(os.path.join(files, file_name), False)
        self.assertEqual(output, ['1', '2', '3'])

#-----------------------------------------------------------------------------
