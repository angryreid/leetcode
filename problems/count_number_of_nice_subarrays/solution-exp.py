class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Helper function to count subarrays with at most k odd numbers
        def atMost(k):
            count = ans = left = 0  # Initialize count of odd numbers, answer, and left pointer
            for right in range(len(nums)):  # Iterate over the array with the right pointer
                count += nums[right] % 2  # Increment count if the current number is odd
                while count > k:  # If count exceeds k, move the left pointer to reduce the count
                    count -= nums[left] % 2  # Decrement count if the number at left pointer is odd
                    left += 1  # Move the left pointer to the right
                ans += right - left + 1  # Add the number of valid subarrays ending at right
            return ans  # Return the total count of subarrays with at most k odd numbers
        
        # The result is the difference between subarrays with at most k and at most k-1 odd numbers
        return atMost(k) - atMost(k - 1)