# -*- coding: utf-8 -*-

from pyaction.datetime_.objects import *
import unittest
import sys
import os

#-----------------------------------------------------------------------------

here = os.path.abspath(os.path.dirname(__file__))
files = os.path.join(here, 'files')

class TestDatetimeObjects(unittest.TestCase):

    def test_create_dates_list(self):
        dates = create_dates_list('11/01/2020', '11/03/2020')
        self.assertEqual(dates, ['11/01/2020', '11/02/2020', '11/03/2020'])

    def test_time_until_end_of_day(self):
        time_left = time_until_end_of_day()
        self.assertIsInstance(time_left, int)

#-----------------------------------------------------------------------------
