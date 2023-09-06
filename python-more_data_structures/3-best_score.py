def best_score(a_dictionary):
  """
  Finds the key with the highest value in a dictionary.

  Args:
    a_dictionary: The dictionary to search.

  Returns:
    The key with the highest value, or None if the dictionary is empty.
  """

  if not a_dictionary:
    return None

  best_key = next(iter(a_dictionary))
  best_score = a_dictionary[best_key]

  for key, value in a_dictionary.items():
    if value > best_score:
      best_key = key
      best_score = value

  return best_key
