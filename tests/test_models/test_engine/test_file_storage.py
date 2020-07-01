#!/usr/bin/python3
"""Unittest for Base Model class from AirBnB clone python project
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import unittest
import pep8
import os


class TestAmenity(unittest.TestCase):
    """Class test using unittest"""

    @classmethod
    def setUpClass(cls):
        """ set up the class """
        cls.prueba = User()
        cls.prueba.name = "team"
        cls.prueba.age = 25

    @classmethod
    def tearDown(cls):
        """ at the end it del the object """
        del cls.prueba

    def tearDown(self):
        """ at the end it remove the json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """ Verify the documentation """
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_args_kwargs(self):
        """ test args and kwargs input """
        self.assertEqual(self.prueba.name, "team")
        self.assertEqual(self.prueba.age, 25)
        self.assertTrue(hasattr(self.prueba, "name"))
        self.assertTrue(hasattr(self.prueba, "age"))
        self.assertEqual(self.prueba.__class__.__name__, "User")

    def test_all(self):
        """ test all in File Stroage """
        test = FileStorage()
        testall = test.all()
        self.assertIsNotNone(testall)
        self.assertEqual(type(testall), dict)

    def test_new(self):
        """ test new in File Stroage """
        test = FileStorage()
        testall = test.all()
        testnew = User()
        testnew.id = "666"
        testnew.name = "Anticristo"
        test.new(testnew)
        k = "{}.{}".format(testnew.__class__.__name__, testnew.id)
        self.assertIsNotNone(testall[k])

    def test_save(self):
        """ test save in File Stroage """
        test = FileStorage()
        obj = BaseModel()
        test.new(obj)
        testall = test.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """ test reload in File Stroage """
        test = FileStorage()
        with open("file.json", mode="w", encoding="utf-8") as f:
            f.write("The universe is a simulation")
        with open("file.json", mode="r", encoding="utf-8") as j:
            p = j.read()
            self.assertEqual(p, "The universe is a simulation")
            self.assertIs(test.reload(), None)
