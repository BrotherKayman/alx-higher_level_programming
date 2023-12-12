#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""
from base import Base


class Rectangle(Base):
	"""
	Implements Base
	Methods:
		__init__()
	"""
	def __init__(self, width, height, x=0, y=0, id=None):
		"""
        Initialize a Rectangle object with width, height, x, y coordinates, and an optional ID.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle (default is 0).
        - y (int): The y-coordinate of the rectangle (default is 0).
        - id (int or None): Optional ID for the rectangle (default is None).
        """
		super().__init__(id)
		self.width = width
		self.height = height
		self.x = x
		self.y = y

		"""
		getter and setters for width
		Return: width
		"""
	@property
	def width(self):	
		return self.__width
	@width.setter
	def width(self, value):
		"""
		validation
		"""
		if type(value) != int:
			raise TypeError('width must be an integer')
		if value < 0:
			raise ValueError('width must be >= 0')
		self.__width = value

		"""
		getter and setters for hight
		Return: height
		"""
	@property
	def height(self):	
		return self.__height
	@height.setter
	def height(self, value):
		"""
		validation
		"""
		if type(value) != int:
			raise TypeError('height must be an integer')
		if value <= 0:
			raise ValueError('height must be >= 0')
		self.__height = value

		"""
		getter and setters for x
		Return: x
		"""
	@property
	def x(self):	
		return self.__x
	@x.setter
	def x(self, value):
		"""
		validation
		"""
		if type(value) != int:
			raise TypeError('x must be an integer')
		if value < 0:
			raise ValueError('x must be >= 0')
		self.__x = value

		"""
		getter and setters for y
		Return: y
		"""
	@property
	def y(self):	
		return self.__y
	@y.setter
	def y(self, value):
		"""
		validation
		"""
		if type(value) != int:
			raise TypeError('y must be an integer')
		if value < 0:
			raise ValueError('y must be >= 0')
		self.__y = value

#Add area
	def area(self):
		"""
		Returns area value
		"""
		return (self.__width * self.__height)

#Add display
	def display(self):
		"""
		Prints in stdout the instance with the # character
		"""
		#for _ in range(self.height):
		#	print('#' * self.width)
		for _ in range(self.y):  # Print empty lines for y offset
			print('$')

		for _ in range(self.height):  # Print the rectangle rows with '#' considering x offset
			print(' ' * self.x + '#' * self.width + '$', end='\n')
#Add string formatter
	def __str__(self):
		"""
		Rormat string format of a rectangle
		"""
		return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")



#Method that assigns an argument to each attribute
	def __update(self, *args):
		"""
        Update attributes of the rectangle with no-keyword arguments in the following order:
        1st argument: id attribute
        2nd argument: width attribute
        3rd argument: height attribute
        4th argument: x attribute
        5th argument: y attribute
        
        Args:
        - *args (tuple): No-keyword arguments in the specified order.
        """
		if len(args) >= 1:
			self.id = args[0]
		if len(args) >= 2:
			self.width = args[1]
		if len(args) >= 3:
			self.height = args[2]
		if len(args) >= 4:
			self.x = args[3]
		if len(args) >= 5:
			self.y = args[4]

	def update(self, *args, ):
		"""Updates instance attributes via no-keyword & keyword args."""
		# print(args, kwargs)
		if args:
			self.__update(*args)
		elif kwargs:
			self.__update(**kwargs)

def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
