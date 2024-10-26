class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Check if the exponent n is negative
        is_neg = n < 0
        # Take the absolute value of n to simplify calculations
        n = abs(n)
        # Initialize the result multiplier to 1
        mult = 1
        # Loop until n becomes 0
        while n > 0:
            # If n is even, square the base x and halve the exponent n
            if n % 2 == 0:
                x *= x
                n = n // 2
            # If n is odd, decrement n and multiply the result by x
            n -= 1
            mult *= x
        # If the original exponent was negative, return the reciprocal of the result
        return mult if not is_neg else 1 / mult