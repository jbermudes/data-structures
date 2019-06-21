#!/usr/bin/env python3

class LinkedListNode(object):
    def __init__(self, value, node=None):
        self.my_value = value
        self.my_next_node = node

    def get_value(self):
        return self.my_value

    def set_value(self, value):
        self.my_value = value

    def get_next_node(self):
        return self.my_next_node

    def set_next_node(self, node):
        self.my_next_node = node

    def __str__(self):
        return "LinkedListNode value: %s, next: %s" % (str(self.my_value), id(self.get_next_node()))


class LinkedList(object):
    def __init__(self):
        self.my_head = None

    def insert(self, value):
        current_node = self.my_head
        previous_node = None
        new_node = LinkedListNode(value)

        if current_node is None:
            # new list, simply point head to node
            self.my_head = new_node
        else:
            # traverse the list until the end
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.get_next_node()

            # previous node is the last node of the list
            previous_node.set_next_node(new_node)

    def remove(self, value):
        """Remove the object with the specified value"""
        previous_node = None
        current_node = self.my_head
        while current_node is not None:
            if current_node.get_value() == value:
                previous_node.set_next_node(current_node.get_next_node())
                break
            else:
                previous_node = current_node
                current_node = current_node.get_next_node()

    def index_of(self, value):
        current_node = self.my_head
        idx = 0
        while current_node is not None:
            if current_node.get_value() == value:
                break
            else:
                current_node = current_node.get_next_node()
                idx += 1

        return idx
    
    def traverse(self):
        current_node = self.my_head
        while current_node is not None:
            print(current_node)
            current_node = current_node.get_next_node()


if __name__ == "__main__":
    li = LinkedList()
    li.insert(1)
    li.insert(3)
    li.insert(4)
    li.insert(5)
    li.traverse()
    print("remove")
    li.remove(4)
    li.remove(3)
    li.insert(2)
    li.traverse()
