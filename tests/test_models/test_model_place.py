#!/usr/bin/python3
''' Class test Unit place Model  '''
import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place




class TestPlaceModel(unittest.TestCase):
    '''
    unit test class for place model

    '''

    @classmethod
    def setUp(cls):
        ''' 
        set up class test review model

        '''
        cls.pla = Place()
        cls.pla.name = "Paris"

    @classmethod
    def tearDown(cls):
        '''
        clean test after run

        '''
        del cls.pla

    def test_class_exists(self):
        '''
        test if class excits

        '''
        result = "<class 'models.place.Place'>"
        self.assertEqual(str(type(self.pla)), result)

    def test_inheritance_place_model(self):
        '''Test if Place is a subclass and instace of BaseModel.
        '''
        self.assertIsInstance(self.pla, Place)
        self.assertEqual(type(self.pla), Place)
        self.assertEqual(issubclass(self.pla.__class__, BaseModel), True)

    def test_types_place_model(self):
        '''test inheristance from base model
        '''
        self.assertIsInstance(self.pla.name, str)
        self.assertEqual(type(self.pla.name), str)
        self.assertIsInstance(self.pla.id, str)
        self.assertEqual(type(self.pla.id), str)
        self.assertIsInstance(self.pla.user_id, str)
        self.assertIsInstance(self.pla.city_id, str)

        
        self.assertIsInstance(self.pla.amenity_ids, list)
        self.assertIsInstance(self.pla.longitude, float)
        self.assertIsInstance(self.pla.latitude, float)
        self.assertIsInstance(self.pla.price_by_night, int)
        self.assertIsInstance(self.pla.max_guest, int)
        self.assertIsInstance(self.pla.description, str)
        self.assertIsInstance(self.pla.number_rooms, int)
        self.assertIsInstance(self.pla.number_bathrooms, int)

        self.assertIsInstance(self.pla.created_at, datetime.datetime)
        self.assertIsInstance(self.pla.updated_at, datetime.datetime)
        
        

    def test_save_place_model(self):
        '''
        test if updated at work after save

        '''
        self.pla.save()
        self.assertNotEqual(self.pla.created_at, self.pla.updated_at)

    def test_doc_place_review(self):
        '''
        test if place string out works
        '''
        self.assertIsNotNone(Place.__doc__)

    def test_params_place_model(self):
        '''test if params class place model
        '''
        self.assertTrue(hasattr(self.pla, 'name'))
        self.assertTrue(hasattr(self.pla, 'id'))
        self.assertTrue(hasattr(self.pla, 'created_at'))
        self.assertTrue(hasattr(self.pla, 'updated_at'))
        self.assertTrue(hasattr(self.pla, 'city_id'))
        self.assertTrue(hasattr(self.pla, 'user_id'))
        self.assertTrue(hasattr(self.pla, 'description'))
        self.assertTrue(hasattr(self.pla, 'number_rooms'))
        self.assertTrue(hasattr(self.pla, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pla, 'max_guest'))
        self.assertTrue(hasattr(self.pla, 'price_by_night'))
        self.assertTrue(hasattr(self.pla, 'latitude'))
        self.assertTrue(hasattr(self.pla, 'longitude'))
        self.assertTrue(hasattr(self.pla, 'amenity_ids'))

    def test_to_dict_place_model(self):
        '''Test if to_dict method is working correctly.
        '''
        my_model_json = self.pla.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.pla.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.pla.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.pla.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.pla.id)

    def test_id_unique_place_model(self):
        '''Test if each instance is created with a unique ID.
        '''
        pla2 = self.pla.__class__()
        pla3 = self.pla.__class__()
        pla4 = self.pla.__class__()
        pla5 = self.pla.__class__()
        self.assertNotEqual(self.pla.id, pla2.id)
        self.assertNotEqual(self.pla.id, pla3.id)
        self.assertNotEqual(self.pla.id, pla4.id)
        self.assertNotEqual(self.pla.id, pla5.id)


if __name__ == '__main__':
    unittest.main()

