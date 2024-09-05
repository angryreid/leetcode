class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_r = Counter(ransomNote)
        cnt_m = Counter(magazine)

        for ch in ransomNote:
            if cnt_m[ch] < cnt_r[ch]:
                return False
        return True

        