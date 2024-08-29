
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        if n < 2:
            return ans
        stack = []
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                while stack and height[top] == height[stack[-1]]:
                    stack.pop()
                if stack:
                    left = stack[-1]
                    ans += (min(height[left], height[i]) - height[top]) * (i - left -1)
            stack.append(i)
        return ans
        