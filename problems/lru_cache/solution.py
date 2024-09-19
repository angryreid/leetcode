class LRUCache:

    def __init__(self, capacity: int):
        self.maps = {}
        self.head = DoublyLinkedNode(-1)
        self.tail = DoublyLinkedNode(-1)
        self.capacity = capacity
        self.length = 0
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key in self.maps:
            cur = self.maps[key][0]
            pre = cur.pre
            next = cur.next
            pre.next = next
            next.pre = pre
            tmp = self.head.next
            self.head.next = cur
            cur.next = tmp
            tmp.pre = cur
            cur.pre = self.head
            return self.maps[key][1]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            cur = self.maps[key][0]
            pre = cur.pre
            next = cur.next
            pre.next = next
            next.pre = pre
            tmp = self.head.next
            self.head.next = cur
            cur.next = tmp
            tmp.pre = cur
            cur.pre = self.head
            self.maps[key] = [cur, value]
            return
        if self.length == self.capacity:
            denode = self.tail.pre
            denodePre = denode.pre
            denodePre.next = self.tail
            self.tail.pre = denodePre
            del self.maps[denode.val]
            self.length -= 1
        cur = DoublyLinkedNode(key)
        tmp = self.head.next
        self.head.next = cur
        cur.next = tmp
        tmp.pre = cur
        cur.pre = self.head
        self.maps[key] = [cur, value]
        self.length += 1
        
        
class DoublyLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)