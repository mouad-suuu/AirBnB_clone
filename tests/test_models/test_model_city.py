#!/usr/bin/python3
''' 
Class test Unit city Model

'''
import unittest
import datetime
from models.base_model import BaseModel
from models.city import City




class TestCityModel(unittest.TestCase):
    '''
    unit test class for city model
    '''

    @classmethod
    def setUp(clas):
        '''
        set up class test review model
        
        '''

        clas.c = City()
        clas.c.name = "Paris"

    @classmethod
    def tearDown(clas):
        '''
        clean test after run

        '''
        del clas.c

    def test_class_city_model_exists(self):
        '''
        test if class excits

        '''
        res = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.c)), res)

    def test_inheritance_city_model(self):
        '''
        test inheristance from base model

        '''
        self.assertIsInstance(self.c, City)
        self.assertEqual(type(self.c), City)
        self.assertEqual(issubclass(self.c.__class__, BaseModel), True)

    def test_types_city_model(self):
        '''
        test type from city model

        '''
        self.assertIsInstance(self.c.id, str)
        self.assertEqual(type(self.c.id), str)

        self.assertIsInstance(self.c.name, str)
        self.assertEqual(type(self.c.name), str)

        self.assertIsInstance(self.c.state_id, str)

        self.assertIsInstance(self.c.created_at, datetime.datetime)
        self.assertIsInstance(self.c.updated_at, datetime.datetime)
        

    def test_save_city_model(self):
        '''
        test if updated at work after save
        '''
        self.c.save()
        self.assertNotEqual(self.c.created_at, self.c.updated_at)

    def test_doc_city_model(self):
        '''
        test if city string out works

        '''
        self.assertIsNotNone(City.__doc__)

    def test_params_city_model(self):
        '''
        test of params in class review model

        '''
        self.assertTrue(hasattr(self.c, 'name'))
        self.assertTrue(hasattr(self.c, 'id'))
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'created_at'))
        self.assertTrue(hasattr(self.c, 'updated_at'))
        

    def test_to_dict_city_model(self):
        '''
        test if to dict is working

        '''
        my_model_json = self.c.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.c.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.c.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.c.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.c.id)

    def test_id_unique_city_model(self):
        '''
        test if class got unique id from inhersite class
        
        '''
        c2 = self.c.__class__()
        c3 = self.c.__class__()
        c4 = self.c.__class__()
        c5 = self.c.__class__()
        self.assertNotEqual(self.c.id, c2.id)
        self.assertNotEqual(self.c.id, c3.id)
        self.assertNotEqual(self.c.id, c4.id)
        self.assertNotEqual(self.c.id, c5.id)


if __name__ == '__main__':
    unittest.main()

