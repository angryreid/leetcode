class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionaries to keep track of mappings
        s_to_t = {}
        t_to_s = {}
        
        # Iterate over characters in both strings
        for i, ch in enumerate(s):
            # Check if there is a conflicting mapping from s to t
            if ch in s_to_t and s_to_t[ch] != t[i]:
                return False
            # Check if there is a conflicting mapping from t to s
            if t[i] in t_to_s and t_to_s[t[i]] != ch:
                return False
            # Establish the mapping
            s_to_t[ch] = t[i]
            t_to_s[t[i]] = ch
        
        return True