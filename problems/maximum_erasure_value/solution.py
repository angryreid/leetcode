class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 1. define the value to be checked in the sliding window
        sums = 0
        largest = 0
        hash = set()

        # 2. dfine the border of the sliding window, left & right
        start = 0
        for end in range(len(nums)):
            # 3. update the maintaining value, sometime may use if condition to check
            # 4. if the window size is changable, need to check if the window is valid
            # while loop can be used to move the window to be valid
            while nums[end] in hash:
                sums -= nums[start]
                hash.remove(nums[start])
                start += 1
            sums += nums[end]
            hash.add(nums[end])
            largest = max(largest, sums)
        # 5. return maintaining value
        return largest