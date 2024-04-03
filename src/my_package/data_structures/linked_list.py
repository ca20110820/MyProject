from typing import Any


class _Node:
    def __init__(self, data: Any):
        self._data: Any = data
        self._next_pointer: _Node | None = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: Any):
        self._data = value

    @property
    def next_pointer(self):
        return self._next_pointer

    @next_pointer.setter
    def next_pointer(self, value):
        if not isinstance(value, _Node):
            raise TypeError("The Pointer to Next Node must be _Node data type.")

        self._next_pointer = value


class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    @property
    def head(self) -> _Node | None:
        return self._head

    @property
    def tail(self) -> _Node | None:
        return self._tail

    @property
    def length(self) -> int:
        return self._length

    @classmethod
    def from_list(cls, inp_list: list):
        # TODO: Implement an alternative constructor for Linked List with a given list.
        pass

    def __str__(self) -> str:
        temp_list = []
        current_node = self._head
        while current_node is not None:
            temp_list.append(current_node.data)
            current_node = current_node.next_pointer
        return f"{temp_list}"

    def insert_at_start(self, data: Any):
        new_node = _Node(data)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next_pointer = self._head
            self._head = new_node

        self._length += 1  # Update the LinkedList Length

    def insert_at_end(self, data: Any):
        new_node = _Node(data)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next_pointer = new_node  # Modify the Old Tail
            self._tail = new_node  # Assign a New Tail

        self._length += 1

    def insert_after_node(self, prev_node: _Node, data: Any):
        if prev_node is None:
            raise ValueError("Previous Node Cannot be None.")

        new_node = _Node(data)
        new_node.next_pointer = prev_node.next_pointer
        prev_node.next_pointer = new_node
        self._length += 1

    def delete(self, data: Any):
        if self._head is None:
            raise ValueError("List is empty")

        if self._head.data == data:
            self._head = self._head.next_pointer
            self._length -= 1
            return

        current_node = self._head
        while current_node.next_pointer is not None:
            if current_node.next_pointer.data == data:
                current_node.next_pointer = current_node.next_pointer.next_pointer
                if current_node.next_pointer is None:
                    self._tail = current_node
                self._length -= 1
                return
            current_node = current_node.next_pointer

    def delete_at_position(self, position: int):
        if position < 0 or position >= self._length:
            raise IndexError("Invalid position.")

        if position == 0:
            self._head = self._head.next_pointer
            self._length -= 1
            return

        current_node = self._head
        for _ in range(position - 2):
            current_node = current_node.next_pointer
        current_node.next_pointer = current_node.next_pointer.next_pointer
        if current_node.next_pointer is None:
            self._tail = current_node
        self._length -= 1

    def traverse(self):
        current_node = self._head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_pointer

    def search(self, data: Any) -> int | None:
        current_node = self._head
        position = 0
        while current_node is not None:
            if current_node.data == data:
                return position
            current_node = current_node.next_pointer
            position += 1

        return None
