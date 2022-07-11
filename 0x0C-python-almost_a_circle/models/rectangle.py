#!/usr/bin/python3
"""Define a class Base"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Inicialize a rectangle object.

        Parametters:
        ------------
            - width (int): Rectangle's width
            - height (int): Rectangle's height
            - x (int): Rectangle's x position
            - y (int): Rectangle's y position
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter or Setter for Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter or Setter for Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter or Setter for Rectangle's x position"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter or Setter for Rectangle's y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return Rectangle's area"""
        return self.__width * self.__height

    def display(self):
        """
        Print an informal and nicely printable string
        of a Rectangle object.
        """
        mTop = "\n" * self.__y
        mLeft = " " * self.__x
        row = ("#" * self.__width) + "\n"
        print(mTop + ((mLeft + row) * self.__height), end="")

    def __str__(self):
        """Return an informal printable string of a Rectangle object."""
        return "[Rectangle] ({}) {}/{} - {}/{}". format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        if args and len(args) > 0:
            len_args = len(args)

            if len_args >= 1:
                if args[0] is not None:
                    self.id = args[0]
                else:
                    self.__init__(self.width, self.height, self.x, self.y)

            self.width = args[1] if len_args >= 2 else self.width
            self.height = args[2] if len_args >= 3 else self.height
            self.x = args[3] if len_args >= 4 else self.x
            self.y = args[4] if len_args >= 5 else self.y

        elif kwargs and len(kwargs) > 0:
            if "id" in kwargs.keys():
                if kwargs["id"] is not None:
                    self.id = kwargs["id"]
                else:
                    self.__init__(self.width, self.height, self.x, self.y)

            for arg in kwargs.keys():
                if arg in ("width", "height", "x", "y"):
                    setattr(self, arg, kwargs[arg])

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        dic = {}
        ncls = "_Rectangle__"
        for k, v in self.__dict__.items():
            dic.update({str(k[12:]): v}) if ncls in k else dic.update({k: v})
        return dic
