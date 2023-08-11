"""
In this module:
 class Square inherits from class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square which inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square.

           Args:
            width: Square width
            height: Square height
            x: Square x_value
            y: Square y_value
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
         Overrides __str__

         Returns formatted string.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width
    
    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size to be set.
        """
        self.width = self.height = value
   