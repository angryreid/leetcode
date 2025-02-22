class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sets = []
        subsets = []
        
        def backtrack(start):
            if len(subsets) == k:
                sets.append(subsets[:])
                return

            for num in range(start, n + 1):
                subsets.append(num)
                backtrack(num + 1)
                subsets.pop()
        
        backtrack(1)
        return sets