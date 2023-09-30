def inherits_from(obj, a_class):
    some_class = type(obj)
return issubclass(some_class, a_class) and some_class is not a_class
