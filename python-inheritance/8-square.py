Rectangle = __import__("7-rectangle").Rectangle


class BaseGeometryMeta(type):
    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr
    class BaseGeometry(metaclass=BaseGeometryMeta):
    """BaseGeometry Class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)
