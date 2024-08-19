# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to handle edge cases
        dummy.next = head  # Point the dummy node to the head of the list
        cur = dummy  # Initialize the current pointer to the dummy node
        while cur.next != None and cur.next.next != None:  # Traverse the list until the end
            if cur.next.val == cur.next.next.val:  # Check if the current node and the next node have the same value
                val = cur.next.val  # Store the duplicate value
                while cur.next and cur.next.val == val:  # Remove all nodes with the duplicate value
                    cur.next = cur.next.next  # Move the pointer to the next node
            else:
                cur = cur.next  # Move to the next node if no duplicates are found

        return dummy.next  # Return the modified list starting from the original head