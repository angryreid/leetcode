class DoublyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None  # Corrected attribute name

class LRUCache:

    def __init__(self, capacity: int):
        self.maps = {}  # Dictionary to store key-node pairs
        self.head = DoublyLinkedNode(-1)  # Dummy head node
        self.tail = DoublyLinkedNode(-1)  # Dummy tail node
        self.capacity = capacity  # Capacity of the cache
        self.length = 0  # Current length of the cache
        self.head.next = self.tail  # Initialize head's next to tail
        self.tail.prev = self.head  # Initialize tail's prev to head

    def get(self, key: int) -> int:
        if key in self.maps:  # If key is in the cache
            cur = self.maps[key][0]  # Get the node
            # Remove the node from its current position
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # Move the node to the head
            tmp = self.head.next
            self.head.next = cur
            cur.next = tmp
            tmp.prev = cur
            cur.prev = self.head
            return self.maps[key][1]  # Return the value
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.maps:  # If key is already in the cache
            cur = self.maps[key][0]  # Get the node
            # Remove the node from its current position
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # Move the node to the head
            tmp = self.head.next
            self.head.next = cur
            cur.next = tmp
            tmp.prev = cur
            cur.prev = self.head
            self.maps[key] = [cur, value]  # Update the value in the cache
            return
        if self.length == self.capacity:  # If the cache is full
            denode = self.tail.prev  # Get the least recently used node
            denode.prev.next = self.tail  # Remove the node from the list
            self.tail.prev = denode.prev
            del self.maps[denode.val]  # Remove the key from the cache
            self.length -= 1
        # Add the new node to the head
        cur = DoublyLinkedNode(key)
        tmp = self.head.next
        self.head.next = cur
        cur.next = tmp
        tmp.prev = cur
        cur.prev = self.head
        self.maps[key] = [cur, value]  # Add the key-value pair to the cache
        self.length += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)