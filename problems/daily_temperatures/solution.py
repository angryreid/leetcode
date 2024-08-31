class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = list()

        for i in range(n):
            t = temperatures[i]
            while stack and t > temperatures[stack[-1]]:
                preIdx = stack.pop()
                ans[preIdx] = i - preIdx
            stack.append(i)
        return ans

