
"""
This module defines Class Base
"""

class Base:
     """Base class for managing id attributes
      Attributes:
        __nb_objects (int): Private class attribute to keep track of objects.
        id (int): Public instance attribute representing the object's ID.

      Methods:
        __init__(self, id=None): Constructor for the Base class."""
     __nb_objects = 0

     def __init__(self, id=None):
         """
         Initialize the Base instance.

         Args:
         id (int, optional): The ID value for the instance. Defaults to None.
         """
         if id is not None:
             self.id = id
         else:
             Base.__nb_objects +=1
             self.id = Base.__nb_objects
