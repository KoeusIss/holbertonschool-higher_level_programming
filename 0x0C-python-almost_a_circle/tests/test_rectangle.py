"""TestRectangle module"""
import unittest
from models.base import *
from models.rectangle import *


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""

    def test_create_instance_with_empty_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_create_instance_with_less_number_of_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(4)

    def test_create_instance_with_much_number_of_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_create_instance_with_private_width(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__width

    def test_create_instance_with_private_height(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__height

    def test_create_instance_with_private_x(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__x

    def test_create_instance_with_private_y(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__y

    def test_getter_instance_attribute_width(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)

    def test_getter_instance_attribute_height(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.height, 5)

    def test_getter_instance_attribute_x(self):
        r = Rectangle(3, 5, 6, 7)
        self.assertEqual(r.x, 6)

    def test_getter_instance_attribute_y(self):
        r = Rectangle(3, 5, 6, 7)
        self.assertEqual(r.y, 7)

    def test_create_instance_attribute_with_given_id(self):
        r = Rectangle(3, 4, 5, 6, 43)
        self.assertEqual(r.id, 43)

if __name__ == "__main__":
    unittest.main()
