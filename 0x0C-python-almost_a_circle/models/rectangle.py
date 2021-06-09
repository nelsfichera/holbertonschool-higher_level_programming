#!/usr/bin/python3
'''inherited from base'''
from models.base import Base


class Rectangle(Base):
    '''rectangle class, parent base, child square'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructs the class rectangle'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        '''prints rectangle string to stdout'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height
        )

    @property
    def width(self):
        '''gets width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''gets height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''gets x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''sets x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''gets y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''sets y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''returns the area'''
        return self.__width * self.__height

    def display(self):
        '''prints the rectangle to stdout with #'''
        for y in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def to_dictionary(self):
        '''returns dictionary representation of a rectangle'''
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

    def update(self, *args, **kwargs):
        '''updates rectangle'''
        if (args and args != []):
            key = ["id", "width", "height", "x", "y"]
            for i in range(0, len(args)):
                setattr(self, key[i], args[i])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
