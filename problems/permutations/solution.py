class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
                subsets.append(nums[i])
                used[i] = True

                self.backtrack(nums, sets, subsets, used)
                used[i] = False
                subsets.pop()