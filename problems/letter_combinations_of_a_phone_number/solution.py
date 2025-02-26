class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        
        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def dfs(index, c):
            if index == len(digits):
                res.append(c)
                return
            digit = digits[index]
            letters = phoneMap[digit]
            for lt in letters:
                dfs(index + 1, c + lt)
            
        dfs(0, '')
        return res