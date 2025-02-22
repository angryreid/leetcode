class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Initialize the list to store all combinations
        sets = []
        # Initialize the list to store the current combination
        subsets = []
        
        # Define the backtracking function
        def backtrack(start):
            # If the current combination is complete (length equals k), add it to the list of all combinations
            if len(subsets) == k:
                sets.append(subsets[:])
                return

            # Iterate through all numbers from 'start' to 'n'
            for num in range(start, n + 1):
                # Include the current number in the combination
                subsets.append(num)
                # Continue the backtracking process with the next number
                backtrack(num + 1)
                # Remove the last number to backtrack and explore other combinations
                subsets.pop()
        
        # Start the backtracking process from the number 1
        backtrack(1)
        # Return the list of all combinations
        return sets