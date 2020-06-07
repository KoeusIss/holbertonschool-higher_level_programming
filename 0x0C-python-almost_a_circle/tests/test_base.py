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
        r = Rectangle(10, 7, 2, 8, 255)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = [{"x": 2, "width": 10, "id": 255, "height": 7, "y": 8}]
        self.assertEqual(json_dictionary, expected)
