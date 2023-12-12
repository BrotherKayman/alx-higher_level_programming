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
    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"