#!/usr/bin/python3
"""Unittest for Base Model class from AirBnB clone python project
"""
from models.base_model import BaseModel
import unittest
import pep8
import os


class TestBaseModel(unittest.TestCase):
    """Class test using unittest"""

    @classmethod
    def setUpClass(cls):
        cls.base = BaseModel()
        cls.base.name = "team"
        cls.base.age = 25

    @classmethod
    def tearDown(cls):
        del cls.base

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_BaseModel(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_save(self):
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.update_at)


if __name__ == "__main__":
    unittest.main()
