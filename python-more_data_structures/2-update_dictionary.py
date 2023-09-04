def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})

def print_sorted_dictionary(my_dict):
    if my_dict is not None:
        for key, value in sorted(my_dict.items()):
            print("{}: {}".format(key, value))
