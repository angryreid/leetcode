class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        carry = 0
        while l1 >=0 or l2 >= 0:
            x = int(num1[l1]) if l1 >= 0 else 0
            y = int(num2[l2]) if l2 >= 0 else 0
            print(x)
            total = x + y + carry
            digit = total % 10
            carry = total // 10
            res = str(digit) + res
            l1 -= 1
            l2 -= 1
        if carry != 0:
            res = str(carry) + res
        return res