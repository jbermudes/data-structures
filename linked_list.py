#!/usr/bin/env python3

class LinkedListNode(object):
    def __init__(self, data, node=None):
        self.my_data = data
        self.my_next_node = node

    def get_data(self):
        return self.my_data

    def set_data(self, data):
        self.my_data = data

    def get_next_node(self):
        return self.my_next_node

    def set_next_node(self, node):
        self.my_next_node = node

    def __str__(self):
        return "LinkedListNode value: %s" % str(self.my_data)


class LinkedList(object):
    def __init__(self):
        self.my_head = None

    def insert(self, data):
        current_node = self.my_head
        next_node = None
        new_node = LinkedListNode(data)

        if current_node is None:
            # new list, simply point head to node
            self.my_head = new_node
        else:
            # traverse the list until the end
            while next_node is not None:
                next_node = current_node.get_next_node()
                current_node = next_node

            # current node is now the last node in list
            current_node.set_next_node(new_node)

    def remove(self, value):
        previous_node = None
        current_node = self.my_head
        while current_node is not None:
            if current_node.get_data() == value:
                previous_node.set_next_node(current_node.get_next_node())
            else:
                current_node = current_node.get_next_node()

    def find(self, value):
        current_node = self.my_head
        while current_node is not None:
            if current_node.get_data() == value:
                return current_node
            else:
                current_node = current_node.get_next_node()

        return None
    
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
    li.traverse()
    
