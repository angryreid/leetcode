class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while stack and stack[-1] > p:
                stack.pop()
            if stack:
                ans[i] = p - stack[-1]
            else:
                ans[i] = p
            stack.append(p)
        return ans
