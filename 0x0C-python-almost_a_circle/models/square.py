#!/usr/bin/python3
"""Define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Inicialize a square object.

        Parametters:
        ------------
            - size (int): Square's size
            - x (int): Square's x position
            - y (int): Square's y position
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Getter or Setter for Square's size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return an informal printable string of a Square object."""
        return "[Square] ({}) {}/{} - {}". format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        if args and len(args) > 0:
            len_args = len(args)

            if len_args >= 1:
                if args[0] is not None:
                    self.id = args[0]
                else:
                    self.__init__(self.size, self.x, self.y)

            self.size = args[1] if len_args >= 2 else self.width
            self.x = args[2] if len_args >= 3 else self.x
            self.y = args[3] if len_args >= 4 else self.y

        elif kwargs and len(kwargs) > 0:
            if "id" in kwargs.keys():
                if kwargs["id"] is not None:
                    self.id = kwargs["id"]
                else:
                    self.__init__(self.size, self.x, self.y)

            for arg in kwargs.keys():
                if arg in ("size", "x", "y"):
                    setattr(self, arg, kwargs[arg])

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
