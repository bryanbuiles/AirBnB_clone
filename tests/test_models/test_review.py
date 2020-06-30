#!/usr/bin/python3
"""Unittest for Base Model class from AirBnB clone python project
"""
from models.review import Review
import unittest
import pep8
import os
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Class test using unittest"""

    @classmethod
    def setUpClass(cls):
        cls.prueba = Review()
        cls.prueba.name = "team"
        cls.prueba.age = 25

    @classmethod
    def tearDown(cls):
        del cls.prueba

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        self.assertTrue(len(Review.__init__.__doc__) > 1)

    def test_args_kwargs(self):
        self.assertEqual(self.prueba.name, "team")
        self.assertEqual(self.prueba.age, 25)
        self.assertTrue(hasattr(self.prueba, "name"))
        self.assertTrue(hasattr(self.prueba, "age"))
        self.assertEqual(self.prueba.__class__.__name__, "Review")
