# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        
        dummy_head = ListNode()
        dummy_head.next = head

        sub_len = 1
        while sub_len < n:
            pre = dummy_head
            cur = dummy_head.next

            while cur:
                left_head = cur
                for i in range(1, sub_len):
                    if cur.next:
                        cur = cur.next

                right_head = cur.next
                cur.next = None
                cur = right_head

                for i in range(1, sub_len):
                    if cur and cur.next:
                        cur = cur.next

                next_node = None
                if cur:
                    next_node = cur.next
                    cur.next = None

                merged = self.mergeTwoList(left_head, right_head)

                pre.next = merged

                while pre.next:
                    pre = pre.next

                cur = next_node
            sub_len *= 2
        return dummy_head.next

    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        pre = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return dummy.next
    