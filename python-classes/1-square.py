class Square:
    """Square class with private size attribute."""

    def __init__(self, size=0):
        """
        Class constructor.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Get the square's size."""
        return self.__size

    @size.setter
    def size(self, new_size):
        """Set the square's size."""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_size
