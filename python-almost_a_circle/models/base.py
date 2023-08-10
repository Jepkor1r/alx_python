

"""
This module defines Class Base
"""

class Base:
     __nb_objects = 0

def __init__(self, id=None):
    """
        Initialize the Base instance.

        Args:
            id (int, optional): The ID value for the instance. Defaults to None.
        """
    if id != None:
        self.id = id
    else:
        Base.__nb_objects +=1
        self.id = Base.__nb_objects
