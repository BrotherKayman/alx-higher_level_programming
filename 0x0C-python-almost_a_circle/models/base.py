#!/usr/bin/python3
"""
Class that defines the base
"""
from json import dumps
class Base:
	"""
	Represents the Base model
	Base for all the classes of the project
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

#Save to jason
    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Converts a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): A list containing dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
                 Returns "[]" if the input is None or an empty list.
        '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
