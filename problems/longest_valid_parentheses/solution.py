class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_len = 0
        start = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i + 1
                else:
                    stack.pop()
                    if not stack:
                        max_len = max(max_len, i - start + 1)
                    else:
                        max_len = max(max_len, i - (stack[-1] + 1) + 1)
        return max_len
        