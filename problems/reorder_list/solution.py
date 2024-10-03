# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left = head
        mid = self.findMid(head)
        right = mid.next
        mid.next = None
        right = self.reverseNode(right)

        while left and right:
            left_next = left.next
            right_next = right.next
            left.next = right
            left = left_next
            right.next = left_next
            right = right_next
    
    def findMid(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseNode(self, head):
        if head == None or head.next == None:
            return head
        cur = self.reverseNode(head.next)
        head.next.next = head
        head.next = None
        return cur
        