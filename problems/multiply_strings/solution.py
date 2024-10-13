# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         if num1 == '0' or num2 == '0':
#             return '0'
        
#         m, n = len(num1), len(num2)
#         ans = [0] * (m + n)
        
#         for i in range(m - 1, -1, -1):
#             carry = 0
#             for j in range(n - 1, -1, -1):
#                 product = int(num1[i]) * int(num2[j]) + ans[i + j + 1] + carry
#                 ans[i + j + 1] = product % 10
#                 carry = product // 10
#             ans[i + j] += carry
        
#         ans_str = ''.join(map(str, ans)).lstrip('0')
#         return ans_str if ans_str else '0'

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        ans = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + ans[i + j + 1]
                ans[i + j + 1] = product % 10  # Current digit
                ans[i + j] += product // 10  # Carry

        # Convert the list of numbers to a string, remove leading zeros
        ans_str = ''.join(map(str, ans)).lstrip('0')
        
        return ans_str if ans_str else '0'
