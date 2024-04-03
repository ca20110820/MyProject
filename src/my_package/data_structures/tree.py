class TreeInsertionError(Exception):
    pass


def traverse_node(node):
    yield node

    for child in node.children:
        if child.is_internal:
            yield from traverse_node(child)
        elif child.is_leaf:
            yield child


class Node:
    def __init__(self, label="Node", data=None):
        self._parent = None
        self._children = []
        self._label = label
        self._data = data

    def __str__(self) -> str:
        return f"{self._label}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def children(self):  # Direct Children
        return self._children

    @property
    def num_children(self):  # Direct Children
        return len(self.children)

    @property
    def descendants(self):
        return [child for child in traverse_node(self) if child != self]

    @property
    def nodes(self):  # Get all, including self
        return [node_ for node_ in traverse_node(self)]

    @property
    def edges(self):
        """List of 2-tuples representing the edge from parent to child"""
        return [(self, child) for child in self.children]

    @property
    def is_root(self):
        return self._parent is None

    @property
    def is_leaf(self):
        return len(self._children) == 0

    @property
    def is_internal(self):
        return not (self.is_root or self.is_leaf)

    def insert_child(self, child):
        # assert child not in self._children, "The Node is already a child!"

        if child in self._children:
            TreeInsertionError("The Node is already a child!")

        # Check if inserting a child to this node forms a "cycle".
        for node in traverse_node(child):
            if node == self:
                raise TreeInsertionError(f"Node {self._label} is child or descendant of {child}")

        # Check if the child already have a parent
        if child.parent is not None:
            raise TreeInsertionError(f"The Node already have a parent!")

        self._children.append(child)  # Append the new Child in the Children list

        # Warn: What if the given Child Node has a Parent already?
        child.parent = self  # Set the Child's Parent

    def remove_parent(self):
        self.parent.delete_child(self)
        self.parent = None  # Set this instance's parent to None

    def replace_parent(self, new_parent):
        self.remove_parent()  # Remove the current parent; Raises AttributeError if this instance have no parent
        new_parent.insert_child(self)  # Insert this instance a child for the given parent
        self.parent = new_parent  # Set the New Parent

    def _remove_child(self, child):
        self._children.remove(child)

    def delete_child(self, child):
        child.parent = None
        self._remove_child(child)

    def is_child(self, child):
        return child in self._children

    def is_parent(self, parent):
        return parent == self.parent and self.parent is not None


class Tree:
    def __init__(self, root_node) -> None:
        # Case: Given root_node is root in another tree
        # Case: Given root_node is internal in another tree
        # Case: Given root_node is leaf in another tree

        if root_node is None:
            self._root = Node(label="Root")
        elif isinstance(root_node, str):
            self._root = Node(label=root_node)
        elif isinstance(root_node, Node):
            self._root = root_node

    @property
    def root(self):
        return self._root

    @property
    def nodes(self):
        return [node for node in traverse_node(self._root)]

    @property
    def leaves(self):
        return [node for node in traverse_node(self._root) if node.is_leaf]

    def __str__(self) -> str:
        return str([str(node) for node in self.nodes])

    def is_root(self, node: Node):
        return self._root == node

    def is_internal(self, node: Node):
        if node not in self.nodes:
            raise ValueError("The Given Node does not belong to this tree.")

        # This would work for subtree
        return not self.is_root(node) and not node.is_leaf

    def is_leaf(self, node: Node):
        if node not in self.nodes:
            raise ValueError("The Given Node does not belong to this tree.")

        return node.is_leaf

    def get_subtree(self, node):
        if node not in self.nodes:
            raise ValueError("The Given Node does not belong to this tree.")

        return Tree(node)

    def remove_by_label_pattern(self, label_pattern: str):
        for node in self.nodes:
            if label_pattern.lower() in str(node).lower():
                pass


def get_height(node: Node):
    nodes = [node_ for node_ in traverse_node(node)]
    leaves = [node_ for node_ in traverse_node(node) if node_.is_leaf]

    heights = []
    for leaf in leaves:
        height = 0
        parent = leaf.parent
        child = leaf
        while True:
            if parent in nodes:
                height += 1
                child = parent
                parent = child.parent
            else:
                break

        heights.append(height)

    return max(heights)


def get_path(leaf: Node, node: Node):
    # Returns List[Node]
    leaves = [node_ for node_ in traverse_node(node) if node_.is_leaf]

    if leaf not in leaves:
        raise ValueError(f"{leaf} is not a leaf of {node}")

    nodes = [node_ for node_ in traverse_node(node)]

    out_path = []
    parent = leaf.parent
    child = leaf
    out_path.append(child)
    while True:
        if parent in nodes:
            out_path.append(parent)
            child = parent
            parent = child.parent
        else:
            break

    return list(reversed(out_path))


def get_depth(node: Node, root: Node):
    nodes = [node_ for node_ in traverse_node(root)]

    if node not in nodes:
        raise ValueError("The given node is not part of the given root")

    leaves = [node_ for node_ in traverse_node(root) if node_.is_leaf]

    for leaf in leaves:
        path = get_path(leaf, root)  # From Root to Leaf
        if node in path:
            idx = path.index(node)
            return len(path[:idx + 1]) - 1
