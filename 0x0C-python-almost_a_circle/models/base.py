#!/usr/bin/python3
"""
Class that defines the base
"""
from json import dumps
import csv
import turtle
import time
from random import randrange

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

    @staticmethod
    def from_json_string(json_string):
        '''
        Convert a JSON string to a Python list.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: A list of Python objects represented by the JSON string.
                  Returns an empty list if the input is None or an empty string.
        '''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Save a list of objects as a JSON file.

        Args:
            list_objs (list): List of objects to be saved as JSON.
        '''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        '''
        Load objects from a JSON file.

        Returns:
            list: A list of objects loaded from the JSON file.
                  Returns an empty list if the file doesn't exist or is empty.
        '''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        '''
        Create an instance from a dictionary.

        Args:
            dictionary (dict): Dictionary containing object attributes.

        Returns:
            object: An instance of the class based on the provided dictionary.
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Save objects to a CSV file.

        Args:
            list_objs (list): List of objects to be saved as CSV.
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''
        Load objects from a CSV file.

        Returns:
            list: A list of objects loaded from the CSV file.
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Draw rectangles and squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle objects to be drawn.
            list_squares (list): List of Square objects to be drawn.
        '''
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
