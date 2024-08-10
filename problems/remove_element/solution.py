class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        s = 0
        for f in range(n):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1

        return s