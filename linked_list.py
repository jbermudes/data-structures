#!/usr/bin/env python3

class LinkedListNode(object):
    def __init__(self, value, next_node=None, prev_node=None):
        self.my_value = value
        self.my_next_node = next_node
        self.my_previous_node = prev_node

    def get_value(self):
        return self.my_value

    def set_value(self, value):
        self.my_value = value

    def get_next_node(self):
        return self.my_next_node

    def get_previous_node(self):
        return self.my_previous_node

    def set_next_node(self, node):
        self.my_next_node = node

    def set_previous_node(self, node):
        self.my_previous_node = node

    def __repr__(self):
        return "LinkedListNode value: %s, me: %s prev: %s next: %s" % (str(self.my_value), 
            id(self), id(self.get_previous_node()), id(self.get_next_node()))


class LinkedList(object):
    def __init__(self):
        self.my_head = None
        self.my_tail = None

    def insert(self, value):
        current_node = self.my_head
        previous_node = None
        new_node = LinkedListNode(value)

        if current_node is None:
            # new list, simply point head to node
            self.my_head = new_node
            self.my_tail = new_node
        else:
            # traverse the list until the end
            while current_node is not None:
                previous_node = current_node
                current_node = current_node.get_next_node()

            # previous node is the last node of the list
            # current is None
            previous_node.set_next_node(new_node)
            new_node.set_previous_node(previous_node)
            self.my_tail = new_node

    def remove(self, value):
        """Remove the object with the specified value"""
        previous_node = None
        current_node = self.my_head
        while current_node is not None:
            if current_node.get_value() == value:
                next_node = current_node.get_next_node()

                if previous_node is None:
                    self.my_head = next_node
                else:
                    previous_node.set_next_node(next_node)

                if next_node is None:
                    self.my_tail = previous_node
                else:
                    next_node.set_previous_node(previous_node)

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
    li.remove(4)
    li.remove(3)
    li.insert(2)
    li.traverse()
