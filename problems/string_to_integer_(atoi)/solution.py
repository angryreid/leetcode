class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        top = 2**31 - 1
        bottom = -2**31
        ans = 0
        sign = 1
        index = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if ans > (top - digit) // 10:
                return top if sign == 1 else bottom
            
            ans = ans * 10 + digit
            index += 1

        return sign * ans
