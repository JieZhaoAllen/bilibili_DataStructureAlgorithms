"""
Created by Allen on '2019/4/10 17:38'
头结点，尾节点
"""
__author__ = 'Allen'


class Node:
    """
    节点
    """
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList:

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        ...

    def length(self):
        ...

    def travel(self):
        ...

    def add(self, item):
        self._head = item.next

    def append(self, item):
        ...

    def insert(self, pos, item):
        ...

    def remove(self, item):
        ...

    def search(self, item):
        ...


ll = SingleLinkList()
node = Node(100)

ll.add(node)