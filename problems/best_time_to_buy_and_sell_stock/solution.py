class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        maxi = 0
        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            maxi = max(maxi, prices[i] - mini)
        return maxi