#!/usr/bin/python3
"""
Square class which is an implementation of the Rectangle class.
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class, inheriting from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        
        Parameters:
        - size (int): The size of the square.
        - x (int): X-coordinate of the square's position.
        - y (int): Y-coordinate of the square's position.
        - id (Optional): An identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the value of the size.
        
        Parameters:
        - value (int): The new size value.
        
        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates attributes based on arguments provided.
        Keyword arguments (kwargs) are ignored if args is not empty.

        Parameters:
        - *args: Variable number of non-keyword arguments.
        - **kwargs: Variable number of keyword arguments.
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
        Overrides the str function to provide a custom string representation.
        """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
