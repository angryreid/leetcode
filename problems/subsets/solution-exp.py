class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize the list to store all subsets
        sets = []
        # Initialize the list to store the current subset
        subsets = []
        # Sort the input list to ensure subsets are generated in a sorted order
        nums.sort()
        # Start the backtracking process from the first index
        self.backtrack(nums, 0, sets, subsets)
        # Return the list of all subsets
        return sets

    def backtrack(self, nums, i, sets, subsets):
        # Add a copy of the current subset to the list of all subsets
        sets.append(subsets[:])
        # Iterate through the remaining elements starting from index i
        for j in range(i, len(nums)):
            # Include nums[j] in the current subset
            subsets.append(nums[j])
            # Continue the backtracking process from the next index
            self.backtrack(nums, j + 1, sets, subsets)
            # Remove the last element to backtrack and explore other subsets
            subsets.pop()