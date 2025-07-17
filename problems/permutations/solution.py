class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        cur = []
        used = [False] * n
        def backtrack(level):
            if level == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    backtrack(level + 1)
                    used[i] = False
                    cur.pop()
        backtrack(0)
        return res