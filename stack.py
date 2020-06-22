# An array based stack.

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def push(self, e):
        """Add element to the top of the stack."""
        self._data.append(e)

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        Raise Empty Exception if stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        """
        Remove and return the element at the top of the stack.
        Raise Empty Exception if stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack empty."""
        return (len(self._data)==0)

#Reversing data using stack
def reverse_file(filename):
    """Overwrite given file ith its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename, 'r')
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    #overwrite content in LIFO order.
    output = open(filename, 'w')
    while not S.is_empty():
        output.rite(S.pop() + "\n")
    output.close()