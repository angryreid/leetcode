class Solution:
    def calculate(self, s: str) -> int:
        stack = list()
        sign = 1
        res = 0
        length = len(s)
        i = 0
        while i < length:
            ch = s[i]
            if ch == ' ':
                i += 1
            elif ch.isdigit():
                value = ord(s[i]) - ord('0')
                while i + 1 < length and s[i + 1].isdigit():
                    i += 1
                    value = value * 10 + ord(s[i]) - ord('0')
                res += value * sign
                i += 1
            elif ch == '+':
                sign = 1
                i += 1
            elif ch == '-':
                sign = -1
                i += 1
            elif ch == '(':
                stack.append(res)
                res = 0
                stack.append(sign)
                sign = 1
                i += 1
            elif ch== ')':
                formerSign = stack.pop()
                formerRes = stack.pop()
                res = formerRes + formerSign * res
                i += 1
        return res

        