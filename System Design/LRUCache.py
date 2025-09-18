class Node:
    def __init__(self, query, result):
        self.query = query
        self.result = result
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Maps query to Node

        # Dummy head and tail nodes
        self.head = Node(None, None)  # Most recently used
        self.tail = Node(None, None)  # Least recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Detach node from the linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_to_front(self, node):
        """Insert node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, query):
        if query in self.cache:
            node = self.cache[query]
            self._remove(node)
            self._insert_to_front(node)
            return node.result
        return None

    def set(self, query, result):
        if query in self.cache:
            node = self.cache[query]
            node.result = result
            self._remove(node)
            self._insert_to_front(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove least recently used node
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.query]

            new_node = Node(query, result)
            self.cache[query] = new_node
            self._insert_to_front(new_node)
