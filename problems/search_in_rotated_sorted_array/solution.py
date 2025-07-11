class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            v = nums[mid]
            if v == target:
                return mid
            if nums[l] <= v:
                if nums[l] <= target <= v:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if v <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1