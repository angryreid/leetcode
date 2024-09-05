class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        cnt = {}
        for ch in s:
            if ch not in cnt:
                cnt[ch] = 0
            cnt[ch] += 1
        
        for k, v in cnt.items():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
        return ans + 1 if ans < len(s) else ans

        
        