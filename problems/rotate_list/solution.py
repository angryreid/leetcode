# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        n = 0
        t_head = head
        while t_head:
            t_head = t_head.next
            n += 1
        
        slow, fast = head, head
        k = k % n
        for i in range(k):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = head
        new_head = slow.next
        slow.next = None

        return new_head
        

