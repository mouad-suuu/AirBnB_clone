#!/usr/bin/python3
"""
Test suite for Review class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReviewModel(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.user_id = "user123"
        self.review.place_id = "place456"
        self.review.text = "A wonderful experience!"

    def test_class_exists(self):
        self.assertEqual(str(type(self.review)), "<class 'models.review.Review'>")

    def test_inheritance_review_model(self):
        self.assertIsInstance(self.review, Review)
        self.assertEqual(type(self.review), Review)
        self.assertEqual(issubclass(self.review.__class__, BaseModel), True)

    # Add more test cases based on the attributes and methods of your Review class


if __name__ == '__main__':
    unittest.main()

