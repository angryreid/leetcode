# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        for _ in range(left - 1):
            pre = pre.next
            cur = cur.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = cur.next.next
            temp.next = pre.next
            pre.next = temp
        
        return dummy.next