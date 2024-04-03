"""Module containing implementations of different search algorithms."""


def binary_search(numbers, target):
    """Returns the index of the target number in the list of numbers, if exists.
    Otherwise, it returns -1."""
    # Reference: https://pseudoeditor.com/guides/binary-search
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
