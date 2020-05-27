class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(list(map(str, nodes)))

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __getitem__(self, item):
        if not self.head:
            raise Exception('List is empty')
        if item == 0:
            return self.head

        else:
            for ix,node in enumerate(self):
                if ix == item:
                    return node
        
        raise Exception(str(item),'is not in list')

    def add_first(self, node):
        node = Node(node)
        node.next = self.head
        self.head = node

    def add_last(self, node):
        node = Node(node)
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        new_node = Node(new_node)
        if not self.head:
            raise Exception('List is empty')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        new_node = Node(new_node)
        if not self.head:
            raise Exception('List is empty')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')
        if self.head == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)