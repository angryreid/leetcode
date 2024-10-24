from typing import List  # Importing List from the typing module for type hinting

class Solution:
    def rob(self, nums: List[int]) -> int:  # Define the method rob that takes a list of integers
        n = len(nums)  # Get the number of houses (length of the list)
        
        dp = [0] * n  # Initialize a dynamic programming array to store maximum values
        
        if n == 1:  # If there is only one house
            return nums[0]  # Return the value of that house
        
        if n == 2:  # If there are two houses
            return max(nums[0], nums[1])  # Return the maximum value between the two houses
        
        dp[0] = nums[0]  # The maximum value for the first house is its own value
        dp[1] = max(nums[0], nums[1])  # The maximum value for the first two houses
        
        # Iterate from the third house to the second last house
        for i in range(2, n - 1):
            # Calculate the maximum value by either skipping the current house or robbing it
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        max_n = dp[n - 2]  # Store the maximum value obtained by robbing up to the second last house

        dp2 = [0] * n  # Initialize a second dynamic programming array for the second scenario
        dp2[1] = nums[1]  # The maximum value for the first house in this scenario is the second house's value

        # Iterate from the third house to the last house
        for i in range(2, n):
            # Calculate the maximum value for this scenario
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        
        # Return the maximum value between the two scenarios
        return max(max_n, dp2[n - 1])  
