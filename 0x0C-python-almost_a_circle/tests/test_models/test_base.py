#!/usr/bin/python3
""" Testcase for Base class module file"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseClassMethods(unittest.TestCase):
    """ Test the Base class methods"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default_value(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_for_nb_objects(self):
        """ Test nb object attribute """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_mixture(self):
        """ Test nb object attributes and assigned id """
        obj1 = Base()
        obj2 = Base(1024)
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 1024)
        self.assertEqual(obj3.id, 2)

    def test_string_id(self):
        """ Test string id """
        obj = Base('1')
        self.assertEqual(obj.id, '1')

    def test_more_arguments_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            obj = Base(1, 1)

    def test_access_private_attributes(self):
        """ Test accessing to private attributes """
        obj = Base()
        with self.assertRaises(AttributeError):
            obj.__nb_objects

    def test_save_to_json_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        result = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), result)

        try:
            os.remove("Square.json")
        except Exception:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_json_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
