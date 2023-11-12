#!/usr/bin/python3
"""
Test suite for Place class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.place.name = "Paris"

    def test_class_exists(self):
        self.assertEqual(str(type(self.place)), "<class 'models.place.Place'>")

    def test_inheritance_place_model(self):
        self.assertIsInstance(self.place, Place)
        self.assertEqual(type(self.place), Place)
        self.assertEqual(issubclass(self.place.__class__, BaseModel), True)

    # Add more test cases based on the attributes and methods of your Place class


if __name__ == '__main__':
    unittest.main()

