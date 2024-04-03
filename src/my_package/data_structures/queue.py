class Queue:
    def __init__(self, initializer=None):
        self._list = initializer or []

    @property
    def peek(self):
        return self._list[-1] if len(self._list) > 0 else None

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return f"{self._list}"

    def get_item_at_index(self, idx):
        return self._list[idx]

    def enqueue(self, elem):
        self._list.append(elem)

    def dequeue(self):
        self._list = self._list[1:]
