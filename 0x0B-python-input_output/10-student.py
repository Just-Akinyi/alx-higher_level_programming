#!/usr/bin/python3
"""Define Student class"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Inicialize a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance"""

        if type(attrs) == list and all(type(i) == str for i in attrs):
            k_v = [[k, getattr(self, k)] for k in attrs if hasattr(self, k)]
            return dict(k_v)
        return self.__dict__
