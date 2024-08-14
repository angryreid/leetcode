# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head.next
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
        if head.next != None:
            s2 = head.next
            f2 = head.next.next
            while f2 != None and f2.next != None:
                f2 = f2.next.next
                s2 = s2.next
            if s != s2:
                return s2
        return s
        