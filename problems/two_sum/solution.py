class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i, v in enumerate(nums):
            last = target - v
            if last in remain:
                return [remain[last], i]
            remain[v] = i
        return Null
        