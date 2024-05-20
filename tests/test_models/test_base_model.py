#!/usr/bin/python3
"""
Unittests for the BaseModel class.
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class.
    """
    def test_for_kwargs_as_attribute(self):
        """
        Tests for kwargs as attributes.
        """
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        self.assertEqual(model.name, "Holberton")
        self.assertEqual(model.my_number, 89)

    def test_BaseModel_attributes(self):
        """Tests for Base_model attributes"""
        self.assertIsInstance(BaseModel().id, str)
        self.assertIsInstance(BaseModel().updated_at, datetime.datetime)
        self.assertIsInstance(BaseModel().created_at, datetime.datetime)

    def test_save_method_of_BaseModel_attr(self):
        """Before save method is called."""
        model = BaseModel()
        previous = model.updated_at
        model.save()
        """After save method is called."""
        current = model.updated_at
        self.assertNotEqual(previous, current)

    def test_if_to_dict_contains_all_key(self):
        """Tests if dictionary contains all keys."""
        dict_cont = BaseModel().to_dict()
        self.assertIn('__class__', dict_cont)
        self.assertIsInstance(dict_cont['created_at'], str)
        self.assertIsInstance(dict_cont['updated_at'], str)


if "_name_" == "_main_":
    unittest.main()
