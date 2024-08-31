class Solution:
    # 2024-08-31
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        if n < 2:
            return ans
        stack = []
        for i in range(n):
            
            while stack and height[i] > height[stack[-1]]:
                top = stack[-1]
                while stack and height[stack[-1]] == height[top]:
                    stack.pop()
                if stack:
                    left = stack[-1]
                    ans += (min(height[left], height[i]) - height[top]) * (i - left -1)
            stack.append(i)
        return ans
        