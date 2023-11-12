#!/usr/bin/python3
''' Class test Unit amenity Model '''
import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity




class TestAmenity(unittest.TestCase):
    '''Defines tests for Amenity Class'''

    @classmethod
    def setUp(clas):
        '''
        set up class test amenity model

        '''
        clas.a = Amenity()
        clas.a.name = "Paris"

    @classmethod
    def tearDown(clas):
        '''
        clean test after run

        '''
        del clas.a

    def test_class_amenity_model(self):
        '''
        test if class excits

        '''
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_inheritance_amenity_model(self):
        '''
        test inheristance from base model

        '''
        self.assertIsInstance(self.a, Amenity)
        self.assertEqual(type(self.a), Amenity)
        self.assertEqual(issubclass(self.a.__class__, BaseModel), True)

    def test_types_amenity_model(self):
        '''
        test type from amenity model

        '''
        self.assertIsInstance(self.a.name, str)
        self.assertEqual(type(self.a.name), str)
        self.assertIsInstance(self.a.id, str)
        self.assertEqual(type(self.a.id), str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)

    def test_save_amenity_model(self):
        '''
        test if updated at work after save

        '''
        self.a.save()
        self.assertNotEqual(self.a.created_at, self.a.updated_at)

    def test_doc_amenity_model(self):
        '''
        test if review string out works

        '''
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        '''Test if expected attributes exist.
        '''
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_to_dict_amenity_model(self):
        '''
        test if to dict is working

        '''
        mj = self.a.to_dict()
        self.assertEqual(str, type(mj['created_at']))
        self.assertEqual(mj['created_at'],self.a.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.a.created_at))
        self.assertEqual(mj['__class__'],self.a.__class__.__name__)
        self.assertEqual(mj['id'], self.a.id)

    def test_unique_id(self):
        '''Test if each instance is created with a unique ID.
        '''
        a2 = self.a.__class__()
        a3 = self.a.__class__()
        a4 = self.a.__class__()
        a5 = self.a.__class__()
        self.assertNotEqual(self.a.id, a2.id)
        self.assertNotEqual(self.a.id, a3.id)
        self.assertNotEqual(self.a.id, a4.id)
        self.assertNotEqual(self.a.id, a5.id)


if __name__ == '__main__':
    unittest.main()

