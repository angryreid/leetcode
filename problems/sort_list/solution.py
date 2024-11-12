# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        itr = head

        nums = []
        while itr:
            nums.append(itr.val)
            itr = itr.next
        
        nums.sort()
        itr = head
        for i in nums:
            itr.val = i
            itr = itr.next

        return head   