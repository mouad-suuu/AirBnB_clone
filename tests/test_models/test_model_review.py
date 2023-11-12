#!/usr/bin/python3
''' 
Class test Unit review Model 

'''
import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review




class TestReviewModel(unittest.TestCase):
    '''unit test class for review model'''

    @classmethod
    def setUp(clas):
        '''
        set up class test review model
        '''
        clas.rev = Review()
        clas.rev.name = "Paris"

    @classmethod
    def tearDown(clas):
        '''
        clean test after run

        '''
        del clas.rev

    def test_class_review_model_exists(self):
        '''
        test if class excits

        '''
        res = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.rev)), res)

    def test_inheritance_review_model(self):
        '''
        test inheristance from base model

        '''
        self.assertIsInstance(self.rev, Review)
        self.assertEqual(type(self.rev), Review)
        self.assertEqual(issubclass(self.rev.__class__, BaseModel), True)

    def test_types_review_model(self):
        '''
        test type from review model

        '''
        self.assertIsInstance(self.rev.id, str)
        self.assertEqual(type(self.rev.id), str)

        self.assertIsInstance(self.rev.user_id, str)
        self.assertIsInstance(self.rev.place_id, str)

        self.assertIsInstance(self.rev.text, str)

        self.assertIsInstance(self.rev.created_at, datetime.datetime)
        self.assertIsInstance(self.rev.updated_at, datetime.datetime)
        
        
        
    def test_save_review_model(self):
        '''
        test if updated at work after save

        '''
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_doc_review_model(self):
        '''
        test if review string out works

        '''
        self.assertIsNotNone(Review.__doc__)

    def test_params_review_model(self):
        '''
        test of params in class review model

        '''
        self.assertTrue(hasattr(self.rev, 'id'))
        self.assertTrue(hasattr(self.rev, 'user_id'))

        self.assertTrue(hasattr(self.rev, 'place_id'))

        self.assertTrue(hasattr(self.rev, 'text'))

        self.assertTrue(hasattr(self.rev, 'created_at'))
        self.assertTrue(hasattr(self.rev, 'updated_at'))
        
        
        

    def test_to_dict_review_model(self):
        '''
        test if to dict is working

        '''
        mj = self.rev.to_dict()
        self.assertEqual(str, type(mj['created_at']))
        self.assertEqual(mj['created_at'],self.rev.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.rev.created_at))

        self.assertEqual(mj['__class__'],self.rev.__class__.__name__)
        self.assertEqual(mj['id'], self.rev.id)

    def test_id_unique_review_model(self):
        '''
        test if class got unique id from inhersite class
        
        '''
        rev2 = self.rev.__class__()
        rev3 = self.rev.__class__()
        rev4 = self.rev.__class__()
        rev5 = self.rev.__class__()
        self.assertNotEqual(self.rev.id, rev2.id)
        self.assertNotEqual(self.rev.id, rev3.id)
        self.assertNotEqual(self.rev.id, rev4.id)
        self.assertNotEqual(self.rev.id, rev5.id)


if __name__ == '__main__':
    unittest.main()

