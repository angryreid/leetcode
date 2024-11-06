class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = collections.defaultdict(int)
        for ch in t:
            map[ch] += 1
        
        window_len = len(s) + 1
        left = 0
        right = 0
        count = len(t)
        start = 0

        while right < len(s):
            c = s[right]
            if map[c] > 0:
                count -= 1
            map[c] -= 1

            while count == 0:
                if right - left + 1 < window_len:
                    window_len = right - left + 1
                    start = left
                if map[s[left]] == 0:
                    count += 1
                map[s[left]] += 1
                left += 1
            right += 1
        return '' if window_len == (len(s) + 1) else s[start: start + window_len]