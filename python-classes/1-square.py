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
        self.size = size  # Public size attribute

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square"""
        return self.size ** 2
