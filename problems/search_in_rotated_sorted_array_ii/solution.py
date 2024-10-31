class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            v = nums[mid]

            if target == v:
                return True
            if v == nums[left]: # This line is essential for ensuring that the algorithm can handle duplicates effectively and avoid infinite loops. If you want to optimize the code further, consider other strategies, but this specific check is important for the correctness of the algorithm in the presence of duplicates.
                left += 1
                continue

            if v > nums[left]:
                if nums[left] <= target <= v:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if v <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
