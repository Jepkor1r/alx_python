#!/usr/bin/python3

"""
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.

    Public Methods:
    - area(self): Calculate the area of the geometry.
        Raises:
            NotImplementedError: This method is not implemented in the base class.

    - integer_validator(self, name, value): Validate an integer value.
        Parameters:
            name (str): The name of the value being validated (assumed to be a string).
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
    """
class BaseGeometry:
    """
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            NotImplementedError: This method is not implemented in the base class.
        """
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Parameters:
            name (str): The name of the value being validated (assumed to be a string).
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")