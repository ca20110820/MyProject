"""Set Module"""


class Set:
    """Custom Set Data Structure"""

    def __init__(self):
        self.elem_dict = {}

    def __str__(self):
        return f"Set({list(self.elem_dict.values())})"

    def add(self, elem):
        hash_value = hash(elem)  # Extract the hash value of the new element, which is the Hashable element itself
        self.elem_dict[hash_value] = elem
        # Note: If the item element already exist, we are just reassigning with the same value.

    def remove(self, elem):
        hash_value = hash(elem)  # Extract the hash value of the new element, which is the Hashable element itself
        if hash_value in self.elem_dict.keys():
            del self.elem_dict[hash_value]

    def __contains__(self, elem) -> bool:
        hash_value = hash(elem)  # Extract the hash value of the new element, which is the Hashable element itself
        return hash_value in self.elem_dict.keys()

    def __len__(self):
        return len(self.elem_dict)
