"""TestBase module"""
import unittest
from models.base import *


class TestBase(unittest.TestCase):
    """Tests the base class"""

    def setUp(self):
        """Settigs up instance"""
        self.__a = Base()
        self.__b = Base(42)

    def test_creation_base_instance(self):
        self.assertIsInstance(self.__a, Base)

    def test_creation_base_instance_without_id_arg(self):
        self.assertEqual(self.__a.id, 3)

    def test_creation_two_base_instance_without_id_arg(self):
        self.assertEqual(self.__a.id, 4)

    def test_creation_base_instance_with_id_arg(self):
        self.assertEqual(self.__b.id, 42)

if __name__ == "__main__":
    unittest.main()
