#!/usr/bin/python3
"""Module of tests for amenity"""

import json
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Testing amenity class"""

    def test_types(self):
        """ Checking types are ok"""
        classtest = FileStorage()
        self.assertEqual(type(classtest), FileStorage)

    def test_newinstances(self):
        """ Test class creation """

        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()

        self.assertEqual(type(a), Amenity)
        self.assertEqual(type(b), BaseModel)
        self.assertEqual(type(c), City)
        self.assertEqual(type(p), Place)
        self.assertEqual(type(r), Review)
        self.assertEqual(type(s), State)
        self.assertEqual(type(u), User)

        storage.new(a)
        storage.new(b)
        storage.new(c)
        storage.new(p)
        storage.new(r)
        storage.new(s)
        storage.new(u)

        self.assertIn("{}.{}, {}"
                      .format(a.__class__.__name__,
                              a.id, storage.all().keys()))
        self.assertIn("{}.{}, {}"
                      .format(b.__class__.__name__,
                              b.id, storage.all().keys()))
        self.assertIn("{}.{}, {}"
                      .format(c.__class__.__name__,
                              c.id, storage.all().keys()))
        self.assertIn("{}.{}, {}"
                      .format(p.__class__.__name__,
                              p.id, storage.all().keys()))
        self.assertIn("{}.{}, {}"
                      .format(r.__class__.__name__,
                              r.id, storage.all().keys()))
        self.assertIn("{}.{}, {}"
                      .format(s.__class__.__name__,
                              s.id, storage.all().keys()))
        self.assertIn("{}.{}, {}"
                      .format(u.__class__.__name__,
                              u.id, storage.all().keys()))

    def test_existmethods(self):
        """ Test that methods exist """

        classtest = FileStorage()

        self.assertTrue(hasattr(classtest, "all"), True)
        self.assertTrue(hasattr(classtest, "new"), True)
        self.assertTrue(hasattr(classtest, "save"), True)
        self.assertTrue(hasattr(classtest, "reload"), True)

    def test_allmethod(self):
        """ Test that method all gives a dict"""
        self.assertTrue(type(storage.all()), dict)

    def test_savingmethod(self):
        """ Tests that save is correctly working"""

        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()

        storage.new(a)
        storage.new(b)
        storage.new(c)
        storage.new(p)
        storage.new(r)
        storage.new(s)
        storage.new(u)
        storage.save()

        with open('file.json') as file:
            obj = file.read()

            self.assertIn("{}.{}, {}"
                          .format(a.__class__.__name__, a.id, obj))
            self.assertIn("{}.{}, {}"
                          .format(b.__class__.__name__, b.id, obj))
            self.assertIn("{}.{}, {}"
                          .format(c.__class__.__name__, c.id, obj))
            self.assertIn("{}.{}, {}"
                          .format(p.__class__.__name__, p.id, obj))
            self.assertIn("{}.{}, {}"
                          .format(r.__class__.__name__, r.id, obj))
            self.assertIn("{}.{}, {}"
                          .format(s.__class__.__name__, s.id, obj))
            self.assertIn("{}.{}, {}"
                          .format(u.__class__.__name__, u.id, obj))


if __name__ == '__main__':
    unittest.main()
