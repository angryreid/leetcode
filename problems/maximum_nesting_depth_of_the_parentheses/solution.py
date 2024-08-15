class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        ans = 0
        for ch in s:
            if ch == "(":
                cnt += 1
                ans = max(ans, cnt)
            elif ch == ")":
                cnt -= 1

        return ans

        