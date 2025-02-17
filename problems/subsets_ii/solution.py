class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sets = []
        subset = []
        self.backtrack(0, nums, subset, sets)
        return sets

    def backtrack(self, i, nums, subset, sets):
        sets.append(subset[:])
        # if i >= len(nums):
        #     return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            subset.append(nums[j])
            self.backtrack(j + 1, nums, subset, sets)
            subset.pop()