class Node(object):
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def remove_from_tail(self):
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None


    def append_to_front(self, node):
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

        if not self.tail:
            self.tail = node


    def move_to_front(self, node):
        if node is self.head:
            return
        
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node    
        self.head = node

        if self.tail is None:
            self.tail = node


class LRUCache(object):

    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.map = {}
        self.list = LinkedList()
        self.size = 0

    def get(self, query):

        node = self.lookup.get(query)

        if not node:
            return None
        
        self.list.move_to_front(node)
        return node.value
    
    def set(self, query, value):
        
        node = self.map.get(query)

        if node:
            node.value = value
            self.list.move_to_front(node)
        else:
            if self.size == self.MAX_SIZE:
                self.list.remove_from_tail()
                del self.map[self.list.tail.query]
            else:
                self.size += 1
            self.map[query] = Node(value)
            self.list.append_to_front(self.map[query])
