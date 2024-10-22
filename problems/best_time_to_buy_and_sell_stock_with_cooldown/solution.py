class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        hold = float('-inf')  # Maximum profit when holding a stock
        sold = 0              # Maximum profit when sold
        cooldown = 0          # Maximum profit in cooldown

        for price in prices:
            # Update the states
            new_hold = max(hold, cooldown - price)  # Buy stock
            new_sold = hold + price                  # Sell stock
            new_cooldown = max(cooldown, sold)      # Cooldown state
            hold, sold, cooldown = new_hold, new_sold, new_cooldown
        return max(sold, cooldown)  # Maximum profit can be in sold or cooldown state

