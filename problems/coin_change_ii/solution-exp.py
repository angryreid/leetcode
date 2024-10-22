class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize a list to store the number of ways to make each amount
        # dp[i] will be the number of ways to make amount i
        dp = [0] * (amount + 1)
        
        # There is one way to make amount 0, which is to use no coins
        dp[0] = 1
        
        # Iterate over each coin in the list of coins
        for coin in coins:
            # For each coin, update the dp array for all amounts from coin to amount
            for x in range(coin, amount + 1):
                # Update the number of ways to make amount x by adding the number of ways to make (x - coin)
                dp[x] += dp[x - coin]
        
        # Return the number of ways to make the given amount
        return dp[amount]