class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        
        # return self.fib(n - 1) + self.fib(n - 2)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # a, b = 0, 1
        # for i in range(n - 1):
        #     a, b = b, a + b
        
        # return b

        if n < 2:
            return n
        
        dp = [-1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
        