#!/usr/bin/python3
"""Unittest for Base Model class from AirBnB clone python project
"""
from models.base_model import BaseModel
import unittest
import pep8
import os


class Test_base_model(unittest.TestCase):
    """Class test using unittest"""

    @classmethod
    def setUpClass(cls):
        cls.prueba = BaseModel()
        cls.prueba.name = "team"
        cls.prueba.age = 25

    @classmethod
    def tearDown(cls):
        del cls.base

    def test_BaseModel(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_save(self):
        self.prueba.save()
        self.assertNotEqual(self.prueba.created_at, self.prueba.update_at)
