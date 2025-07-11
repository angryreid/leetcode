class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        max_pds = ''
        for i in range(len(s)):
            max_pds = max(max_pds, expand(i, i), expand(i, i + 1), key=len)
        return max_pds
