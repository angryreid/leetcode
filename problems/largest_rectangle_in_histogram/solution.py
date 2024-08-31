class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(heights)
        newHeights = [0] * (n + 2)
        newHeights[0] = 0
        newHeights[n + 1] = 0

        for i in range(1, n + 1):
            newHeights[i] = heights[i - 1]
        
        for i in range(n + 2):
            while stack and newHeights[i] < newHeights[stack[-1]]:
                top = stack.pop()
                right = i
                left = stack[-1]
                height = newHeights[top]
                ans = max(ans, height * (right - left - 1))
            stack.append(i)
        return ans
        