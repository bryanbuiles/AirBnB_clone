#!/usr/bin/python3
"""Unittest for Base Model class from AirBnB clone python project
"""
from models.base_model import BaseModel
import unittest
import pep8

class Test_base_model(unittest.TestCase):
    """Class test using unittest"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
    
    def test_base_model(self):
        """Test constructor"""
        

