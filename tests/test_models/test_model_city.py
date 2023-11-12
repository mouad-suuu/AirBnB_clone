#!/usr/bin/python3
"""
Test suite for City class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityModel(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.name = "New York"
        self.city.state_id = "NY"

    def test_class_exists(self):
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")

    def test_inheritance_city_model(self):
        self.assertIsInstance(self.city, City)
        self.assertEqual(type(self.city), City)
        self.assertEqual(issubclass(self.city.__class__, BaseModel), True)

    # Add more test cases based on the attributes and methods of your City class


if __name__ == '__main__':
    unittest.main()
