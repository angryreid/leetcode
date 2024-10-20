class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        m = n + 1
        dp = [0] * m
        dp[0] = 1
        dp[1] = 1
        for i in range(2, m):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]