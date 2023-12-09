#!/usr/bin/python3
"""
Class that defines the base
"""
class Base
"""
Base models for all the classes of the project
attributes:
__nb_objects(int) initialized with 0
"""

__nb_objects = 0

def __init__(self, id=None):
	"""
	Initialize a new Base

	Args: 
		id(int): New base identifier
		"""
	 if id is not None:
	 	self.id = id
	 	else:
	 		Base.__nb_objects += 1
	 		self.id = Base.__nb_objects

