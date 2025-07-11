# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            digit = sum % 10
            digit_node = ListNode(digit)
            cur.next = digit_node
            cur = digit_node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next