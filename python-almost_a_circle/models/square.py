"""
In this module:
 class Square inherits from class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square which inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a rectangle.

           Args:
            width: Rectangle width
            height: Rectangle height
            x: Rectangle x_value
            y: Rectangle y_value
        """
        super().__init__(id, x, y, size, size)
    def __str__(self):
        """
         Overrides __str__

         Returns formatted string.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.xy, self.y, self.width)
    