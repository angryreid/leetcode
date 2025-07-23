class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        used = [False] * n
        
        def backtrack():
            if len(cur) == n:
                res.append(cur.copy())
                return
            
            for i in range(n):  # Always check all indices
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    backtrack()  # No level parameter needed
                    cur.pop()
                    used[i] = False
                    
        backtrack()
        return res