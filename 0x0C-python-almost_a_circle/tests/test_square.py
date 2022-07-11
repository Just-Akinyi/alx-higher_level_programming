#!/usr/bin/python3
"""
Define unittests for Rectanagle class
"""
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquare_init(unittest.TestCase):
    """Test cases for init methods in Square class"""

    def test_correct_args(self):
        s1 = Square(10)
        s2 = Square(1, 11)
        s3 = Square(10, 2, 1, 12)
        s4 = Square(10, id=13, y=1, x=2)

        ts = (s1, s2, s3, s4)
        id1 = s1.id
        l_real = [[ar.width, ar.height, ar.x, ar.y, ar.id] for ar in ts]
        l_exp = [
            [10, 10, 0, 0, id1],
            [1, 1, 11, 0, id1 + 1],
            [10, 10, 2, 1, 12],
            [10, 10, 2, 1, 13]]
        self.assertEqual(l_exp, l_real)

    def test_set_size(self):
        s = Square(1)

        s.size = 2
        l_real = [s.width, s.height, s.x, s.y]
        self.assertEqual([2, 2, 0, 0], l_real)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "-20"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -20

    def test_Incorrect_size(self):
        tTypeError = (1.2, "1", True, None)
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Square(case)

        tValueError = (-1, 0)
        for case in tValueError:
            with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Square(case)

    def test_Incorrect_x(self):
        tTypeError = ((1, 1.2), (1, "1"), (1, True), (1, None))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Square(case[0], case[1])

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -3)

    def test_Incorrect_y(self):
        tTypeError = (
            (1, 2, 1.2),
            (1, 2, "1"),
            (1, 2, True),
            (1, 2, None))
        for case in tTypeError:
            with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Square(case[0], case[1], case[2])

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, y=-3)


class TestSquare_area(unittest.TestCase):
    """Test case for area method in Square class"""

    def test_area(self):
        ra = Square(5, 2, 6)
        self.assertEqual(25, ra.area())


class TestSquare_printMethods(unittest.TestCase):
    """Test case for display method in Square class"""

    @patch('builtins.print')
    def test_display_normal(self, mock_print):
        Square(4).display()
        exp1 = "####\n" * 4
        mock_print.assert_called_with(exp1, end="")

    @patch('builtins.print')
    def test_display_position(self, mock_print):
        Square(2, 2, 2).display()
        exp1 = "\n\n" + ("  ##\n" * 2)
        mock_print.assert_called_with(exp1, end="")

        Square(3, 1).display()
        exp2 = (" ###\n" * 3)
        mock_print.assert_called_with(exp2, end="")

    def test_str(self):
        str1 = str(Square(4, 2, 1, 12))
        self.assertEqual("[Square] (12) 2/1 - 4", str1)


class TestSquare_update(unittest.TestCase):
    """Test case for area method in Square class"""

    def test_update_args(self):
        s = Square(1, 3, 4)
        _id = s.id
        s.update(None)
        self.assertEqual("[Square] ({}) 3/4 - 1".format(_id + 1), str(s))

        s.update(12)
        self.assertEqual("[Square] (12) 3/4 - 1", str(s))
        s.update(13, 5)
        self.assertEqual("[Square] (13) 3/4 - 5", str(s))
        s.update(15, 8, 10)
        self.assertEqual("[Square] (15) 10/4 - 8", str(s))
        s.update(16, 11, 13, 14)
        self.assertEqual("[Square] (16) 13/14 - 11", str(s))

    def test_update_kwargs(self):
        s = Square(1, 3, 4)
        _id = s.id
        s.update(id=None)
        self.assertEqual("[Square] ({}) 3/4 - 1".format(_id + 1), str(s))

        s.update(id=12)
        self.assertEqual("[Square] (12) 3/4 - 1", str(s))
        s.update(size=5, id=13)
        self.assertEqual("[Square] (13) 3/4 - 5", str(s))
        s.update(id=15, x=10, size=8)
        self.assertEqual("[Square] (15) 10/4 - 8", str(s))
        s.update(y=14, id=16, x=13, size=11)
        self.assertEqual("[Square] (16) 13/14 - 11", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Test case for to_dictionary method in Square class"""

    def test_area(self):
        s = Square(10, 2, 1)
        exp = {'id': s.id, 'x': 2, 'size': 10, 'y': 1}
        real = s.to_dictionary()
        self.assertEqual(exp, real)
