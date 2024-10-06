class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the list is empty, return the head (which is None)
        if not head:
            return head
        
        # Initialize the length of the list to 0
        n = 0
        # Temporary pointer to traverse the list
        t_head = head
        # Traverse the list to calculate its length
        while t_head:
            t_head = t_head.next
            n += 1
        
        # Initialize two pointers, slow and fast, to the head of the list
        slow, fast = head, head
        # Calculate the effective rotations needed (k modulo n)
        k = k % n
        # Move the fast pointer k steps ahead
        for i in range(k):
            fast = fast.next
        
        # Move both pointers until fast reaches the end of the list
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Link the end of the list to the head to form a cycle
        fast.next = head
        # The new head is the next node after slow
        new_head = slow.next
        # Break the cycle by setting the next of slow to None
        slow.next = None

        # Return the new head of the rotated list
        return new_head