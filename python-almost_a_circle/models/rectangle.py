""""
 In this module:
 Rectangle class inherits from Base class
"""
from models.base import Base


class Rectangle:
    """Rectangle class which inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None,):
        """Initialize a rectangle.

        Args:
            width: Rectangle width
            height: Rectangle height
            x: Rectangle x_value
            y: Rectangle y_value
            id: Rectangle Id 
        """
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getting the Rectangle width"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """Setting the Rectangle width"""
        self.__width = value

    @property
    def height(self):
        """Getting the Rectangle Heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the Rectangle height"""
        self.__height = value

    @property
    def x(self):
        """Getting the Rectangle x_value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the Rectangle x_value"""
        self.__x = value

    @property
    def y(self):
        """Getting the Rectangle y_value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the Rectangle y_value"""
        self.__y = value
