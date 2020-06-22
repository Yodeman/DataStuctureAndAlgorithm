
class Empty(Exception):
    pass

class LinkedStack:
    """LIFO Stack implmentation using a singly linked list for storage."""

    class _Node:
        """Non-public class for storing singly linked node."""

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Retun the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        """
        Remove and return the element at the top of the stack (i.e LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head.next
        self._size -= 1
        return answer