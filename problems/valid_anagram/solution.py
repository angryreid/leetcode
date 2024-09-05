class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        for ch in s:
            if cnt_s[ch] != cnt_t[ch]:
                return False
        return True
        