class BaseGeometry:
    def __dir__(self) -> None:
        attributes = super().__dir__()
        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]
        def area(self):
        raise Exception("area() is not implemented")
