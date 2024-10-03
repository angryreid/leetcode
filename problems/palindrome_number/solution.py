class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = list(str(x))
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        