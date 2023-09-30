def is_kind_of_class(obj, a_class):
    some_class = type(obj)
     if issubclass(some_class, a_class) == True:
        return True
    else:
        return False
