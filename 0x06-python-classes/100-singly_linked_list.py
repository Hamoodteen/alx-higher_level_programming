#!/usr/bin/python3
""" Node """


class Node:
    """ Declare """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

""" Linked list """


class SinglyLinkedList:
    """ Declare """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        a = Node(value)
        if self.head is None or value < self.head.data:
            a.next_node = self.head
            self.head = a
        else:
            ptr = self.head
            while ptr.next_node is not None and ptr.next_node.data <= value:
                ptr = ptr.next_node
            a.next_node = ptr.next_node
            ptr.next_node = a
