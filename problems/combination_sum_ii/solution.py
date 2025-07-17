class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        all_list = []
        cur_list = []
        candidates.sort()

        def backtrack(remaining, level):
            if remaining < 0:
                return
            if remaining == 0:
                all_list.append(cur_list.copy())
                return

            for i in range(level, len(candidates)):
                if i > level and candidates[i] == candidates[i - 1]:
                    continue
                cur_list.append(candidates[i])
                backtrack(remaining - candidates[i], i + 1)
                cur_list.pop()
            
        
        backtrack(target, 0)
        return all_list