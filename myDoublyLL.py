class Empty(Exception):
    pass

class Node:

    def __init__(self, element, prev=None, next=None):
        self._element = element
        self._next = next
        self._prev = prev

    __slots__ = "_element", "_prev", "_next"

class DoublyLinkedList:

    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def empty(self):
        return self._size == 0

    def add_before(self, element, target):
        """Add element before target."""
        if self.empty():
            raise Empty("List is empty")
        else:
            new_node = Node(element, target._prev, target)
            target._prev._next = new_node
            target._prev = new_node

    def add_after(self, element, target):
        """Add element after target."""
        if self.empty():
            raise Empty("List is empty")
        else:
            new_node = Node(element, target, target._next)
            target._next._prev = new_node
            target._next = new_node


    def add(self, element, target=None):
        if self.empty():
            self._head = Node(element)
        elif self._size <= 1:
            self._tail = Node(element, self._head)
            self._head._next = self._tail
        else:
            if target:
                self.add_after(element, target)
