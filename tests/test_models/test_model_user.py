#!/usr/bin/python3
"""
Test suite for User class
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = "john_doe"
        self.user.email = "john_doe@example.com"
        self.user.password = "secure_password"

    def test_class_exists(self):
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def test_inheritance_user_model(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(type(self.user), User)
        self.assertEqual(issubclass(self.user.__class__, BaseModel), True)

    # Add more test cases based on the attributes and methods of your User class


if __name__ == '__main__':
    unittest.main()

