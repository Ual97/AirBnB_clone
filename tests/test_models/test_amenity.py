#!/usr/bin/python3
"""Module of tests for amenity"""

import json
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Testing amenity class"""

    def test_types(self):
        """ Checking types are ok"""
        classtest = Amenity()
        self.assertEqual(type(classtest), Amenity)
        self.assertEqual(type(classtest.id), str)
        self.assertEqual(type(classtest.created_at), datetime)
        self.assertEqual(type(classtest.updated_at), datetime)
        self.assertEqual(type(classtest.__str__()), str)
        self.assertNotEqual(len(classtest.__str__()), 0)
        self.assertEqual(type(classtest.name), str)
        self.assertEqual(str(classtest), "[Amenity] ({}) \
{}".format(classtest.id, classtest.__dict__))

    def test_methods(self):
        """ Testing methods inherited"""
        classtest = Amenity()
        self.assertEqual(type(classtest.to_dict()), dict)
