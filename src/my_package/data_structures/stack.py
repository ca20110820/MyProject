"""Stack Module"""


class Stack:
    """Stack Data Structure"""

    def __init__(self, initializer=None):
        self._list = initializer or []

    def __str__(self):
        return f"{self._list}"

    @property
    def top(self):
        return self._list[-1]

    def pop(self):
        return self._list.pop(-1) if len(self._list) > 0 else None

    def append(self, elem):
        self._list.append(elem)
