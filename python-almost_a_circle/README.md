## PYTHON - ALMOST A CIRCLE

## Table of Contents

- [Introduction ]
- [Rectangle Class]
- [Attributes ]
- [Methods ]

## Introduction
 In this Project, we'll cover the `Rectangle` class, which inherits from the `Base` class and represents rectangles with specific properties.

   # Args and Kwargs
In Python, functions can accept a variable number of arguments. `args` and `kwargs` are common terms used to represent this flexibility:

- `args`: This is used to pass a variable number of non-keyword arguments to a function. They are received as a tuple within the function.
- `kwargs`: This is used to pass a variable number of keyword arguments (i.e., arguments that are specified with a name) to a function. They are received as a dictionary within the function.

   # JSON Encoder and Decoder
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. Python provides built-in modules for encoding Python objects into JSON format (json.dumps()) and decoding JSON data back into Python objects (json.loads()).

Example:

python
Copy code
import json

data = {"key": "value"}
json_data = json.dumps(data)  # Encoding Python object to JSON
decoded_data = json.loads(json_data)  # Decoding JSON data to Python object

   # Unittest Module
The unittest module is part of Python's standard library and provides a framework for writing and executing unit tests. Unit tests help ensure that individual components or functions of your code are working as expected.

Example:

import unittest

class TestExample(unittest.TestCase):
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()

## Rectangle Class

The `Rectangle` class inherits from the `Base` class and represents rectangles with specific attributes such as width, height, position (x and y), and an ID. It provides methods for calculating area, displaying the rectangle, updating attributes, and more.

### Attributes

- `width`: Width of the rectangle.
- `height`: Height of the rectangle.
- `x`: X-coordinate position of the rectangle.
- `y`: Y-coordinate position of the rectangle.
- `id`: Unique identifier of the rectangle inherited from the `Base` class.

### Methods

- `area()`: Calculates the area of the rectangle.
- `display()`: Displays the rectangle using `#` characters.
- `__str__()`: Provides a formatted string representation of the rectangle's attributes.
- `update()`: Updates attributes of the rectangle instance based on provided arguments or keyword arguments

HAPPY CODING!