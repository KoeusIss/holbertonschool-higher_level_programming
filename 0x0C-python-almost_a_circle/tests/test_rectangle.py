"""TestRectangle module"""
import unittest
from models.base import *
from models.rectangle import *


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""

    def test_create_instance_with_empty_args(self):
        """tests empty args"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_create_instance_with_less_number_of_args(self):
        """tests exception raise with lack arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle(4)

    def test_create_instance_with_much_number_of_args(self):
        """tests exception raises with excess of arguments"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_create_instance_with_private_width(self):
        """tests exception raises for calling private attribute"""
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__width

    def test_create_instance_with_private_height(self):
        """tests exception raises for calling private attribute"""
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__height

    def test_create_instance_with_private_x(self):
        """tests exception raises for calling private attribute"""
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__x

    def test_create_instance_with_private_y(self):
        """tests exception raises for calling private attribute"""
        with self.assertRaises(AttributeError):
            r = Rectangle(5, 6)
            r.__y

    def test_getter_instance_attribute_width(self):
        """tests getting and setting width"""
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)

    def test_getter_instance_attribute_height(self):
        """test getting and setting height"""
        r = Rectangle(3, 5)
        self.assertEqual(r.height, 5)

    def test_getter_instance_attribute_x(self):
        """test getting and setting x"""
        r = Rectangle(3, 5, 6, 7)
        self.assertEqual(r.x, 6)

    def test_getter_instance_attribute_y(self):
        """test getting and setting y"""
        r = Rectangle(3, 5, 6, 7)
        self.assertEqual(r.y, 7)

    def test_create_instance_attribute_with_given_id(self):
        """tests getting and setting id"""
        r = Rectangle(3, 4, 5, 6, 43)
        self.assertEqual(r.id, 43)

    def test_raises_type_error_for_non_integer_width(self):
        """tests validation for non integer width"""
        with self.assertRaises(TypeError) as te:
            r = Rectangle("a", 4)
            self.assertEqual("width must be an integer", str(te.exception))

    def test_raises_type_error_for_non_integer_height(self):
        """tests validation for non integer height"""
        with self.assertRaises(TypeError) as te:
            r = Rectangle(4, "A")
            self.assertEqual("height must be an integer", str(te.exception))

    def test_raises_type_error_for_non_integer_x(self):
        """tests validation for non integer x"""
        with self.assertRaises(TypeError) as te:
            r = Rectangle(4, 5, "a")
            self.assertEqual("x must be an integer", str(te.exception))

    def test_raises_type_error_for_non_integer_y(self):
        """tests validation for non integer y"""
        with self.assertRaises(TypeError) as te:
            r = Rectangle(4, 5, 6, "a")
            self.assertEqual("y must be an integer", str(te.exception))

    def test_raises_type_error_for_non_positive_integer_width(self):
        """tests validation for non positive integer width"""
        with self.assertRaises(ValueError) as te:
            r = Rectangle(-3, 4)
            self.assertEqual("width must be > 0", str(te.exception))

    def test_raises_type_error_for_non_positive_integer_height(self):
        """tests validation for non positive integer height"""
        with self.assertRaises(ValueError) as te:
            r = Rectangle(4, -5)
            self.assertEqual("height must be > 0", str(te.exception))

    def test_raises_type_error_for_non_zero_integer_width(self):
        """tests validation for non positive integer width"""
        with self.assertRaises(ValueError) as te:
            r = Rectangle(0, 4)
            self.assertEqual("width must be > 0", str(te.exception))

    def test_raises_type_error_for_non_zero_integer_height(self):
        """tests validation for non positive integer height"""
        with self.assertRaises(ValueError) as te:
            r = Rectangle(4, 0)
            self.assertEqual("height must be > 0", str(te.exception))

    def test_raises_type_error_for_non_positive_integer_x(self):
        """tests validation for non positive integer x"""
        with self.assertRaises(ValueError) as te:
            r = Rectangle(3, 4, -5)
            self.assertEqual("x must be >= 0", str(te.exception))

    def test_raises_type_error_for_non_positive_integer_y(self):
        """tests validation for non positive integer y"""
        with self.assertRaises(ValueError) as te:
            r = Rectangle(3, 4, 5, -6)
            self.assertEqual("y must be >= 0", str(te.exception))

if __name__ == "__main__":
    unittest.main()
