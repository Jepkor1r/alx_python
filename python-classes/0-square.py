#!/usr/bin/python3

class Square:
    """
    This class represents a square with a given size.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return 4 * self.__size

    def get_size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    def set_size(self, new_size):
        """
        Sets the size of the square to a new value.

        Args:
            new_size (int): The new size to set.

        Raises:
            ValueError: If the new size is negative.
        """
        if new_size < 0:
            raise ValueError("Size cannot be negative.")
        self.__size = new_size
        
    