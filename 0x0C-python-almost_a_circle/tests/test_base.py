"""TestBase module"""
import unittest
from models.base import *
from models.rectangle import *
from models.square import *


class TestBase(unittest.TestCase):
    """Tests the base class"""

    def setUp(self):
        """Settigs up instance"""
        self.__a = Base()
        self.__b = Base(42)

    def test_creation_base_instance(self):
        """test base instance creation"""
        self.assertIsInstance(self.__a, Base)

    def test_creation_base_instance_without_id_arg(self):
        """test base instance creation without id"""
        self.assertEqual(self.__a.id, 3)

    def test_creation_two_base_instance_without_id_arg(self):
        """test base instance creation without id"""
        self.assertEqual(self.__a.id, 4)

    def test_creation_base_instance_with_id_arg(self):
        """test base instance creatin with given id"""
        self.assertEqual(self.__b.id, 42)

    def test_returns_json_dictionary(self):
        """tests dictionary serializing"""
        r = Rectangle(10, 7, 2, 8, 255)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        for j in json_dictionary:
            self.assertIsInstance(j, str)

    def test_writing_json_string_to_file(self):
        """tests writing json string"""
        r1 = Rectangle(10, 7, 2, 8, 255)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            the_file = f.read()
        self.assertNotEqual(the_file, "")

    def test_from_json_string_method(self):
        """tests from_json_string method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        expected_output = [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ]
        self.assertEqual(expected_output, list_input)

