class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_list = []
        cur_list = []
        def dfs(level):
            if len(cur_list) == k:
                all_list.append(cur_list.copy())
            
            for i in range(level, n + 1):
                cur_list.append(i)
                dfs(i + 1)
                cur_list.pop()
        dfs(1)
        return all_list