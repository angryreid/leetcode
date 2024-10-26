class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ans = x
        # for i in range(n)
        is_neg = n < 0
        n = abs(n)
        mult = 1
        while n > 0:
            if n % 2 == 0:
                x *= x
                n = n // 2
            n -= 1
            mult *= x
        return mult if not is_neg else 1 / mult
