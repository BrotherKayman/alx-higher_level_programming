#!/usr/bin/python3
"""
class Rectangle that inherits from Base
"""
from models.base import Base

class Rectangle(Base):
	"""
	Implements Base
	Methods:
		__init__()
	"""
	def __init__(self, width, height, x=0, y=0, id=None):
		"""
		Assign arguments to the right attributes 
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
	def update(self, *args):
		"""Update attributes with no-keyword arguments."""
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