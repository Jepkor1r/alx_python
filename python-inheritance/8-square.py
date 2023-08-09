#!usr/bin/python3

"""
    This module that defines the Rectangle and Square classes.
"""


class BaseGeometryMetaClass(type):
    """
    A base class representing geometry.
    """

    def __dir__(cls):
        """
        Metaclass fix
        """
        return[
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__'
            ]

Rectangle = __import__("7-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Public Methods:
    - __init__(self, size): Initialize a square with size.
    """

    def __init__(self, size):
        """
        Initialize a square with size.

        Parameters:
            size (int): The size of the square (both width and height).
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __dir__(cls):
        """
        Metaclass fix
        """
        return[
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]      