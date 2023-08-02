#!/usr/bin/python3

"""
    Check if the given object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Parameters:
        obj: Any Python object.
        a_class: A Python class or class name to compare the type of the object against.

    Returns:
        bool: True if the object is an instance of a subclass of the specified class; otherwise, False.

    Example:
        >>> class Animal:
        ...     pass
        ...
        >>> class Dog(Animal):
        ...     pass
        ...
        >>> class Cat(Animal):
        ...     pass
        ...
        >>> class Bird:
        ...     pass
        ...
        >>> obj1 = Dog()
        >>> obj2 = Cat()
        >>> obj3 = Bird()
        >>>
        >>> inherits_from(obj1, Animal)
        True
        >>> inherits_from(obj2, Animal)
        True
        >>> inherits_from(obj3, Animal)
        False
    """
def inherits_from(obj, a_class):
    """
     Check if the given object is an instance of a class that inherited (directly or indirectly)
     from the specified class.
    """
    return  isinstance(obj, type) and issubclass(obj, a_class)
