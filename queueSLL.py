class Empty(Exception):
    pass

class LinkedQueue:
    """FIFO queue implementation using a signly linked list for storage."""

    class _Node:
        """None-publi class for storing a singly linked list node."""

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elemnts in the queue."""
        return self._size

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def first(self):
        """Return but do not remove element at the front of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        """
        Remove and return the first element of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, elem):
        """Add an element to the back of queue."""
        new_node = self._Node(elem, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1