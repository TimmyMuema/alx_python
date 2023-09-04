def multiple_returns(sentence):
    """Returns the length and first character of a sentence."""

    length = len(sentence)
    first_char = None
    if length > 0:
        first_char = sentence[0]

    return length, first_char
