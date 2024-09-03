class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, v in enumerate(nums):
            if v in seen and i - seen[v] <= k:
                return True
            seen[v] = i
        return False
        