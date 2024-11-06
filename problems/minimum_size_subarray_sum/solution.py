class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')  # Initialize to infinity
        sums = 0
        left = 0
        
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= target:
                current_length = right - left + 1
                min_len = min(min_len, current_length)
                sums -= nums[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len  # Return 0 if no valid subarray found
