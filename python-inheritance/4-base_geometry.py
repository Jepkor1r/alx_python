#!/usr/bin/python3

"""
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.
    """
class BaseGeometry:
    """
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.
    """
    def __dir__(self):
        """
        Customization of the attributes visible when calling `dir()`.

        Excludes the 'area' method from the list of attributes.
        """
        return [attribute for attribute in super().__dir__() if attribute != 'area']

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            NotImplementedError: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
    