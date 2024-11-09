class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        needs = [0] * 26
        for ch in p:
            idx = ord(ch) - ord('a')
            needs[idx] += 1
        window = [0] * 26
        start = 0
        for end in range(len(s)):
            cur = s[end]
            window[ord(cur) - ord('a')] += 1
            if window == needs:
                res.append(start)
            if end >= len(p) - 1:
                chr = s[start]
                window[ord(chr) - ord('a')] -= 1
                start += 1
        return res