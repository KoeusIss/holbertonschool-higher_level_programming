"""TestRectangle module"""
import unittest
import unittest.mock
import sys
import io
from models.base import *
from models.rectangle import *


class TestFirstRectangle(unittest.TestCase):
    """Tests the first Rectangle class"""

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

class TestValidateAttributes(unittest.TestCase):
    """tests validates attributes class"""

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

class TestAreaFirst(unittest.TestCase):
    """Tests area first class"""

    def test_area_for_rectangle_with_three_and_two(self):
        """tests a rectagle area"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_for_rectangle_with_two_and_ten(self):
        """tests a rectagle area"""
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

    def teset_area_for_rectangle_with_all_args(self):
        """tests a rectagle area"""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

class TestDisplay(unittest.TestCase):
    """tests display rectangle"""
    pass

class TestStrRepresentation(unittest.TestCase):
    """tests __str__ overriding methods"""

    def test_str_representation(self):
        r = Rectangle(4, 6, 2, 1, 12)
        str_r = r.__str__()
        self.assertEqual(str_r, "[Rectangle] (12) 2/1 - 4/6")

    def test_str_representation_with_default_value(self):
        r = Rectangle(4, 6)
        str_r = r.__str__()
        self.assertEqual(str_r, "[Rectangle] (11) 0/0 - 4/6")

class TestUpdate(unittest.TestCase):
    """Tests rectangle update"""

    def setUp(self):
        self.r = Rectangle(10, 10, 10, 10)

    def tearDown(self):
        del self.r

    def test_updates_id_attributes(self):
        """tests id attribute update"""
        self.r.update(98)
        self.assertEqual(self.r.id, 98)

    def test_updates_width_attributes(self):
        """tests width attribute update"""
        self.r.update(98, 2)
        self.assertEqual(self.r.width, 2)

    def test_updates_height_attributes(self):
        """tests height attribute update"""
        self.r.update(98, 2, 3)
        self.assertEqual(self.r.height, 3)

    def test_updates_x_attributes(self):
        """tests x attribute update"""
        self.r.update(98, 2, 3, 4)
        self.assertEqual(self.r.x, 4)

    def test_updates_y_attributes(self):
        """tests y attribute update"""
        self.r.update(98, 2, 3, 4, 5)
        self.assertEqual(self.r.y, 5)
