#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

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
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __str__(self):
        output = ""
        point = self.__head

        while point is not None:
            output += str(point.data)
            if point.next_node is not None:
                output += "\n"
            point = point.next_node

        return output

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        point = self.__head

        while point is not None:
            if point.data > value:
                break
            ptr_prev = point
            point = point.next_node

        newNode = Node(value, point)
        if point == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
