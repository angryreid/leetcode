class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, s = 0, len(height) - 1, 0
        max_l, max_r = 0, 0
        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            if max_l <= max_r:
                s += max_l - height[l]
                l += 1
            else:
                s += max_r - height[r]
                r -= 1
        return s