""""
 In this module:
 Rectangle class inherits from Base class
"""
from base import Base


class Rectangle:

    def __init__(self, width, height, x=0, y=0, id=None,):
        """Initialize a rectangle.

        Args:
            width: Rectangle width
            height: Rectangle height
            x: Rectangle x_value
            y: Rectangle y_value
            id: Rectanle Id 
        """
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        self._validate_width()
        self._validate_height()
        self._validate_x()
        self._validate_y()

    @property
    def width(self):
        """Getting the Rectangle width"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """Setting the Rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting the Rectangle Heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the Rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting the Rectangle x_value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting the Rectangle x_value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting the Rectangle y_value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting the Rectangle y_value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def _validate_width(self):
        """Validating the width attribute"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    def _validate_height(self):
        """Validating the height attribute"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    def _validate_x(self):
        """Validating the x attribute"""
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    def _validate_y(self):
        """Validating the y attribute"""
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        
    def area(self):
        """
        Calculating the Rectangle area

        Returns:
            int: The calculated Rectangle area.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using '#'.

        Returns:
            None.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    
    def __str__(self):
        """
        Overrides __str__

        Returns:
            formatted string of Rectange attributes.
        """
        return("[Rectangle] ({}) {}/{} - {}/{}").format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Update attributes of the Rectangle instance
        """
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.__width = args[1]
            if num_args >= 3:
                self.__height = args[2]
            if num_args >= 4:
                self.__x = args[3]
            if num_args >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
