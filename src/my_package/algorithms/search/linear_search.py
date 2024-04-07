""" Module containing implementations of Linear Search Algorithm. """


def linear_search(numbers, target):
    """
    Returns the index of the target number in the list of numbers, if exists.
    Otherwise, it returns -1.
    """
    for i, v in enumerate(numbers):
        if v == target:
            return i
    return -1
