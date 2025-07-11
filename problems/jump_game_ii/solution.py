class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = end = 0
        max_reach = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == end:
                jumps += 1
                end = max_reach
        return jumps