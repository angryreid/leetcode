class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = []
        subsets = []
        used = [False] * len(nums)
        self.backtrack(nums, sets, subsets, used)
        return sets
    
    def backtrack(self, nums, sets, subsets, used):
        if len(subsets) == len(nums):
            sets.append(subsets[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    continue
                subsets.append(nums[i])
                used[i] = True
                self.backtrack(nums, sets, subsets, used)
                used[i] = False
                subsets.pop()
