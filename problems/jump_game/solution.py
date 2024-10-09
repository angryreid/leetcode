class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump = [0] * n
        for i in range(n):
            jump[i] = i + nums[i]

        i = 0
        max_jump = jump[0]
        while i < n and i <= max_jump:
            if jump[i] > max_jump:
                max_jump = jump[i]
            i += 1
        if i >= n:
            return True
        
        return False