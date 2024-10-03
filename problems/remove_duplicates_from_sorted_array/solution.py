class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        step = 1
        for fast in range(len(nums)):
            if slow < step or nums[fast] != nums[slow - step]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
        