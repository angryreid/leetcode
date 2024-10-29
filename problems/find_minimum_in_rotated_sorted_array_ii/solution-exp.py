class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the left pointer to the start of the list
        left = 0
        # Initialize the right pointer to the end of the list
        right = len(nums) - 1

        # Continue the loop until the left pointer is less than the right pointer
        while left < right:
            # Calculate the middle index to avoid overflow
            mid = left + (right - left) // 2
            # If the middle element is less than the rightmost element,
            # the minimum must be in the left half (including mid)
            if nums[mid] < nums[right]:
                right = mid
            # If the middle element is greater than the rightmost element,
            # the minimum must be in the right half (excluding mid)
            elif nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is equal to the rightmost element,
            # decrement the right pointer to skip the duplicate
            else:
                right -= 1
        # Return the minimum element, which is at the left pointer
        return nums[left]