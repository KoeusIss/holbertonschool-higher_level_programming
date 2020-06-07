"""TestSquare"""
import unittest
from models.base import *
from models.rectangle import *
from models.square import *


class TestSquare(unittest.TestCase):
    """tests Square class"""

    def setUp(self):
        self.s = Square(2)

    def tearDown(self):
        del self.s

    def test_create_instance_of_square(self):
        """Tests instance creation for the square"""
        self.assertIsInstance(self.s, Square)

    def test_str_representation_of_the_square(self):
        """test str representation"""
        str_s = self.s.__str__()
        self.assertEqual(str_s, "[Square] (28) 0/0 - 2")

    # def test_instance_attribute_retrieve_size(self):
    #     """test size retrieve"""
    #     self.assertEqual(self.s.size, 2)

    # def test_super_method_call_from_the_square_class(self):
    #     """test inhertiance work perfctly"""
    #     self.s.update(200, 201, 202, 203)
    #     self.assertEqual(self.s.id, 200)
    #     self.assertEqual(self.size, 201)
    #     self.assertEqual(self.)
