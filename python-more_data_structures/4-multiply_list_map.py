def multiply_list_map(my_list=[], number=0):
  """
  Multiplies each element in a list by a number.

  Args:
    my_list: The list to multiply.
    number: The number to multiply each element by.

  Returns:
    A new list with the multiplied elements.
  """

  if not my_list:
    return []

  multiplied_list = []
  for element in my_list:
    multiplied_list.append(element * number)

  return multiplied_list
