#!/usr/bin/env python3

class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right
    
    @right.setter
    def right(self, node):
        self._right = node

    def print(self):
        if self.left is not None:
            self.left.print()

        print(self)

        if self.right is not None:
            self.right.print()

    def __repr__(self):
        return "BSTNode: %s value: %s left: %s right %s" % (id(self), 
            self.value, id(self.left), id(self.right))


class BSTree(object):
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = BSTNode(value)
        found_position = True
        previous_node = None
        current_node = self.head

        if self.head is None:
            self.head = new_node
        else:
            # all the fun work
            while current_node is not None:
                previous_node = current_node
                if current_node.value > value:
                    current_node = current_node.left
                else: 
                    current_node = current_node.right

            # current node is None,
            # previous node is the parent to be attached
            if previous_node.value > value:
                previous_node.left = new_node
            else:
                previous_node.right = new_node

    def traverse(self):
        if self.head is not None:
            self.head.print()

if __name__ == "__main__":
    bst = BSTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(6)
    bst.traverse()

