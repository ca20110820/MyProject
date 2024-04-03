"""Module implementing the Binary Tree Data Structure."""

from my_package.data_structures.tree import Node, Tree, TreeInsertionError


class BinaryTreeNode(Node):
    def __init__(self, label="Node", data=None):
        super().__init__(label=label, data=data)

    def insert_child(self, child):
        if len(self.children) == 2:
            raise TreeInsertionError("Binary Tree can only have at most 2 children!")

        super().insert_child(child)
