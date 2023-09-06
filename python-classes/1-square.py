# Module documentation
"""
This module defines a Square class with a private size attribute.
"""

# Square class
class Square:

    # Private size attribute
    __size = None

    # Class constructor
    def __init__(self, size=0):
        # Validate the size argument
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = size

    # Public size getter
    @property
    def size(self):
        return self.__size

    # Public size setter
    @size.setter
    def size(self, new_size):
        # Validate the new size
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = new_size
