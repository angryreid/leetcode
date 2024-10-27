class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        res = 0
        bound = (2**31 - 1) // 10
        while x:
            pop = x % 10
            x //= 10
            if res > bound or (res == bound and pop > 7):
                return 0
            res = res * 10 + pop
        return sign * res

