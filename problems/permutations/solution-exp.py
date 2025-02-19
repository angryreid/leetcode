class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize the list to store all permutations
        sets = []
        # Initialize the list to store the current permutation
        subsets = []
        # Initialize a list to track whether an element is used in the current permutation
        used = [False] * len(nums)
        # Start the backtracking process
        self.backtrack(nums, sets, subsets, used)
        # Return the list of all permutations
        return sets
    
    def backtrack(self, nums, sets, subsets, used):
        # If the current permutation is complete (same length as nums), add it to the list of all permutations
        if len(subsets) == len(nums):
            sets.append(subsets[:])
            return
        
        # Iterate through all elements in nums
        for i in range(len(nums)):
            # If the element is not used in the current permutation
            if not used[i]:
                # Include nums[i] in the current permutation
                subsets.append(nums[i])
                # Mark the element as used
                used[i] = True

                # Continue the backtracking process
                self.backtrack(nums, sets, subsets, used)
                # Unmark the element as used (backtrack)
                used[i] = False
                # Remove the last element to backtrack and explore other permutations
                subsets.pop()