#!/usr/bin/python3
'''square class, inherits rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class, it's like almost a rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructs class'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''prints the representation of square'''
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width
        )

    @property
    def size(self):
        '''gets the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the size'''
        self.size_validation(value, "width")
        self.width = value
        self.height = value

    def to_dictionary(self):
        '''returns dictionary representation of the square'''
        return {
            "id": self.id,
            "size": self.__width,
            "x": self.__x,
            "y": self.__y
        }

    def update(self, *args, **kwargs):
        '''updates square'''
        if (args and args != []):
            key = ["id", "size", "x", "y"]
            for i in range(0, len(args)):
                setattr(self, key[i], args[i])
        else:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
