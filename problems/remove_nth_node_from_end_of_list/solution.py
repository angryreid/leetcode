# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
       
        s = dummy
        f = head
        for i in range(n):
            f = f.next
        while f is not None:
            f = f.next
            s = s.next

        s.next = s.next.next

        return dummy.next
        