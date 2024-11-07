class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = []
        needs = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord('a')
            needs[idx] += 1
        
        window = [0] * 26
        start = 0
        for end in range(len(s2)):
            cur = s2[end]
            window[ord(cur) - ord('a')] += 1
            if window == needs:
                return True
            
            if end >= len(s1) - 1:
                chr = s2[start]
                window[ord(chr) - ord('a')] -= 1
                start += 1
        return False