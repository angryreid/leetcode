class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            v = nums[mid]
            if v == target:
                return mid
            if nums[left] <= v:
                if nums[left] <= target <= v:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if v <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1