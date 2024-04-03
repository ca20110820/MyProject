class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __str__(self):
        out_list = []
        for elem in self.table:
            for kvp in elem:
                if len(kvp) == 2:
                    out_list.append(kvp)

        return f"{out_list}"

    def hash_func(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        for kvp in self.table[idx]:
            if kvp[0] == key:
                kvp[1] = value  # Updating/Modifying the Value if key exists
                return

        self.table[idx].append([key, value])

    def get(self, key):
        idx = self.hash_func(key)
        for kvp in self.table[idx]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError(f"Key {key} does not exist")

    def remove(self, key):
        idx = self.hash_func(key)
        for i, kvp in enumerate(self.table[idx]):
            if kvp[0] == key:
                del self.table[idx][i]
                return

        raise KeyError(f"Key {key} does not exist")
