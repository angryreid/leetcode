# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        if head.val != head.next.val:
            rest_node = self.deleteDuplicates(head.next)
            head.next = rest_node
            return head
        else:
            new_node = head.next
            while new_node != None and head.val == new_node.val:
                new_node = new_node.next
            return self.deleteDuplicates(new_node)
        