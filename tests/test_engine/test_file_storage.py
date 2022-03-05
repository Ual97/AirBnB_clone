#!/usr/bin/python3
"""Module of tests for amenity"""

import json
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Testing amenity class"""

    def test_types(self):
        """ Checking types are ok"""
        classtest = FileStorage()
        self.assertEqual(type(classtest), FileStorage)

    def test_methods(self):
        """ Testing methods inherited"""
        classtest = FileStorage()
        self.assertEqual(type(classtest.all), dict)
        self.assertEqual(type(classtest.new), dict)
