class Node:

    def __init__(self, elem, next):
        self._element = elem
        self._next = next

class LinkedList:

    def __init__(self, elem=None):
        self._head = None
        self._tail = None
        self._size = 0
        if elem is not None:
            node = Node(elem, None)
            self._head = node
            self._tail = self._head._next
            self._size = 1

    def __len__(self):
        return self._size

    def add_first(self, elem):
        if self._size == 1:
            self._tail = self._head
        if self.is_empty():
            self._head = Node(elem, None)
        else:
            new_node = Node(elem, self._head)
            #new_node._next = self._head
            self._head = new_node
        self._size += 1

    def add_last(self, elem):
        #print(self._tail._element)
        new_node = Node(elem, None)
        if self.is_empty():
            self._head = Node(elem, None)
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
    
    def is_empty(self):
        return self._size == 0

    def __repr__(self):
        node = self._head
        nodes = []
        while node._next is not None:
            nodes.append(node._element)
            node = node._next
        nodes.append(node._element)
        nodes.append('None')
        print(nodes)
        return ' ->'.join(list(map(str, nodes)))

if __name__ == "__main__":
    lst = LinkedList()
    for i in range(5):
        lst.add_first(i)
    for i in range(7,10):
        lst.add_last(i)
    print(lst)
