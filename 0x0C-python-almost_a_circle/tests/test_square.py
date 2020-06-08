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
        self.s.id = 1
        str_s = self.s.__str__()
        self.assertEqual(str_s, "[Square] (1) 0/0 - 2")

    def test_instance_attribute_getting_size(self):
        """test size getting"""
        self.assertEqual(self.s.size, 2)

    def test_instance_attribute_setting_size(self):
        """test size setting"""
        self.s.size = 10
        self.assertEqual(self.s.size, 10)

    def test_raise_exception_with_non_integer_size(self):
        """tests validation for non integer size"""
        with self.assertRaises(TypeError) as te:
            self.s.size = "10"
            self.assertEqual("width must be an integer", str(te.exception))

    def test_raise_exception_with_negative_size(self):
        """tests validation for null  size"""
        with self.assertRaises(ValueError) as te:
            self.s.size = -10
            self.assertEqual("width must be > 0", str(te.exception))

    def test_raise_exception_with_null_size(self):
        """tests validation for null  size"""
        with self.assertRaises(ValueError) as te:
            self.s.size = 0
            self.assertEqual("width must be > 0", str(te.exception))

    def test_updates_square_id_by_passing_args_tuple(self):
        """Test update id from *args tuple"""
        self.s.update(300)
        self.assertEqual(self.s.id, 300)

    def test_updates_size_by_passing_args_tuple(self):
        """Test update size from *args tuple"""
        self.s.update(300, 1)
        self.assertEqual(self.s.id, 300)
        self.assertEqual(self.s.size, 1)

    def test_update_position_using_kwargs_dictionary(self):
        """Test update position from **kwargs dict"""
        self.s.update(x=12, y=13)
        self.assertEqual(self.s.x, 12)
        self.assertEqual(self.s.y, 13)

    def test_update_square_attribute_using_mixin_args_kwargs(self):
        """Test square attribute using args, and kwargs"""
        self.s.update(75, 76, x=77, y=78)
        self.assertEqual(self.s.id, 75)
        self.assertEqual(self.s.size, 76)
        self.assertEqual(self.s.x, 77)
        self.assertEqual(self.s.y, 78)
