class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        subsets = []
        nums.sort()
        self.backtrack(nums, 0, sets, subsets)
        return sets

    def backtrack(self, nums, i, sets, subsets):
        # if i == len(nums):
        sets.append(subsets[:])
            # return
        for j in range(i, len(nums)):
            subsets.append(nums[j])
            self.backtrack(nums, j + 1, sets, subsets)
            subsets.pop()
