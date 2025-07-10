class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        num_map = {
            '2': 'abc',
            '3': 'edf',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(index, c):
            if index == len(digits):
                res.append(c)
                return
            digit = digits[index]
            letters = num_map[digit]
            for lt in letters:
                dfs(index + 1, c + lt)
        dfs(0, '')
        return res