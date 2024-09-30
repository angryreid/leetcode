class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        t = pattern

        if len(s) != len(t):
            return False
        dict_s = {} # word -> pattern
        dict_t = {} # pattern -> word
        for i in range(len(t)):
            if s[i] in dict_s and dict_s[s[i]] != t[i]:
                return False
            if t[i] in dict_t and dict_t[t[i]] != s[i]:
                return False
            if s[i] not in dict_s:
                dict_s[s[i]] = t[i]
            if t[i] not in dict_t:
                dict_t[t[i]] = s[i]
        return True
        