class Solution:
    # return str(bin(int(a, 2) + int(b, 2)))[2:] # due to the result binary will be conducted as 0b1011
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        len_a = len(a) - 1
        len_b = len(b) - 1
        while len_a >= 0 or len_b >= 0 or carry:
            s = carry

            if len_a >= 0:
                s += int(a[len_a])
                len_a -= 1
            
            if len_b >= 0:
                s += int(b[len_b])
                len_b -= 1
            
            ans = str(s % 2) + ans
            carry = s >> 1 # s // 2
        return ans
        