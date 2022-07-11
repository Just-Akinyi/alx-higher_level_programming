#!/usr/bin/python3
"""
Define unittests for Base class
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init(unittest.TestCase):
    """Test cases for init function in Base class"""

    def test_id_None(self):
        b1 = Base()
        _id = b1.id
        b2 = Base()
        b3 = Base(None)
        l_id = [b1.id, b2.id, b3.id]
        self.assertEqual([_id, _id + 1, _id + 2], l_id)

    def test_id_number(self):
        self.assertEqual(55, Base(55).id)

    def test_id_mix(self):
        b4 = Base()
        _id = b4.id
        b9 = Base(9)
        b5 = Base()
        l_id = [b4.id, b9.id, b5.id]
        self.assertEqual([_id, 9, _id + 1], l_id)


class TestBase_to_json_string(unittest.TestCase):
    """Test cases for to_json_string method in Base class"""

    def test_list_dict_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_list_dict_empty(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_correct_list_dict(self):
        r1 = Rectangle(10, 7, 2, 8)
        dic1 = r1.to_dictionary()
        r2 = Rectangle(20, 14, 4, 16)
        dic2 = r2.to_dictionary()

        json_dictionary = Base.to_json_string([dic1, dic2])
        self.assertEqual(str, type(json_dictionary))

        exp = [
            {"x": 2, "width": 10, "id": r1.id, "height": 7, "y": 8},
            {"x": 4, "width": 20, "id": r2.id, "height": 14, "y": 16}
            ]
        real = eval(json_dictionary)
        self.assertEqual(exp, real)


class TestBase_save_to_file(unittest.TestCase):
    """Test cases for save_to_file method in Base class"""

    @classmethod
    def clean_files(self):
        """Clean any 'class.json' files"""

        # os.remove("Square.json")
        # os.remove("Rectangle.json")
        # os.remove("Base.json")
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_list_obj_None(self):
        TestBase_save_to_file.clean_files()

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        TestBase_save_to_file.clean_files()

    def test_list_obj_empty(self):
        TestBase_save_to_file.clean_files()

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        TestBase_save_to_file.clean_files()

    def test_correct_list_obj(self):
        TestBase_save_to_file.clean_files()

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])
        expr = [
            {"y": 8, "x": 2, "id": r1.id, "width": 10, "height": 7},
            {"y": 0, "x": 0, "id": r2.id, "width": 2, "height": 4}
            ]
        with open("Rectangle.json", "r") as file:
            realr = eval(file.read())
        self.assertEqual(expr, realr)

        s1 = Square(10, 2, 8)
        s2 = Square(2, 4)

        Square.save_to_file([s1, s2])
        exps = [
            {"y": 8, "x": 2, "id": s1.id, "size": 10},
            {"y": 0, "x": 4, "id": s2.id, "size": 2}
            ]
        with open("Square.json", "r") as file:
            reals = eval(file.read())
        self.assertEqual(exps, reals)
        TestBase_save_to_file.clean_files()

    def test_overwrite(self):
        TestBase_save_to_file.clean_files()

        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        exp1 = [{"y": 8, "x": 2, "id": r1.id, "width": 10, "height": 7}]
        with open("Rectangle.json", "r") as file:
            real1 = eval(file.read())
        self.assertEqual(exp1, real1)

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        exp2 = [{"y": 0, "x": 0, "id": r2.id, "width": 2, "height": 4}]
        with open("Rectangle.json", "r") as file:
            real2 = eval(file.read())
        self.assertEqual(exp2, real2)
        TestBase_save_to_file.clean_files()

    def test_inherence(self):
        TestBase_save_to_file.clean_files()

        s = Square(2, 4)

        Square.save_to_file([s])
        exps = [{"y": 0, "x": 4, "id": s.id, "size": 2}]
        with open("Square.json", "r") as file:
            reals = eval(file.read())
        self.assertEqual(exps, reals)

        Rectangle.save_to_file([s])
        expb = [{"y": 0, "x": 4, "id": s.id, "size": 2}]
        with open("Rectangle.json", "r") as file:
            realb = eval(file.read())
        self.assertEqual(expb, realb)

        Base.save_to_file([s])
        expb = [{"y": 0, "x": 4, "id": s.id, "size": 2}]
        with open("Base.json", "r") as file:
            realb = eval(file.read())
        self.assertEqual(expb, realb)
        TestBase_save_to_file.clean_files()


class TestBase_from_json_string(unittest.TestCase):
    """Test cases for from_json_string method in Base class"""

    def test_json_string_None(self):
        list_output = Square.from_json_string(None)
        self.assertEqual([], list_output)

    def test_josn_string_empty(self):
        list_input = []
        json_list_input = Square.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual([], list_output)

    def test_correct_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
            ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(list, type(list_output))
        self.assertEqual(list_input, list_output)


class TestBase_crate(unittest.TestCase):
    """Test cases for create method in Base class"""
    def test_create_square(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)

        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)
        self.assertFalse(s1 is s2)

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)


class TestBase_load_from_file(unittest.TestCase):
    """Test cases for load_from_file method in Base class"""

    def test_load_none_file(self):
        list_squares_output = Square.load_from_file()
        self.assertEqual([], list_squares_output)
