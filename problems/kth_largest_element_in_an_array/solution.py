class Solution:
    def findKthLargest(self, nums, k):
        # If the list is empty, return None
        if not nums: return
        
        # Choose a random pivot element from the list
        pivot = random.choice(nums)
        
        # Partition the list into three parts:
        # 'left' contains elements greater than the pivot
        left = [x for x in nums if x > pivot]
        # 'mid' contains elements equal to the pivot
        mid = [x for x in nums if x == pivot]
        # 'right' contains elements less than the pivot
        right = [x for x in nums if x < pivot]
        
        # Calculate the lengths of the 'left' and 'mid' lists
        L, M = len(left), len(mid)
        
        # If k is less than or equal to the length of 'left',
        # the k-th largest element is in the 'left' list
        if k <= L:
            return self.findKthLargest(left, k)
        # If k is greater than the length of 'left' plus the length of 'mid',
        # the k-th largest element is in the 'right' list
        # Adjust k by subtracting the lengths of 'left' and 'mid'
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        # If k is within the range of the 'mid' list,
        # the k-th largest element is the pivot (any element in 'mid')
        else:
            return mid[0]