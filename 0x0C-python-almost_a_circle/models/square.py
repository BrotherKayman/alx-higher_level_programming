#!/usr/bin/python3
"""
Contains the Square class, which implements the Rectangle class.
"""

from rectangle import Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate (default is 0).
            y (int): y-coordinate (default is 0).
            id (int): Identifier (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): New size for the square.
        """
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """
        Internal method that updates instance attributes via *args and **kwargs.

        Args:
            id (int): New identifier value (default is None).
            size (int): New size value (default is None).
            x (int): New x-coordinate value (default is None).
            y (int): New y-coordinate value (default is None).
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.width = size
            self.height = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """
        Updates instance attributes via positional and keyword arguments.

        Args:
            *args: Positional arguments for id, size, x, y.
            **kwargs: Keyword arguments for id, size, x, y.
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Square object.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}