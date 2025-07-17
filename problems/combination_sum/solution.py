class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []
        cur = []
        def backtrack(target, level):
            if target < 0:
                return
            if target == 0:
                res.append(cur.copy())
                return
            for i in range(level, n):
                if target - candidates[i] >= 0:
                    cur.append(candidates[i])
                    backtrack(target - candidates[i], i)
                    cur.pop()
            
        backtrack(target, 0)
        return res