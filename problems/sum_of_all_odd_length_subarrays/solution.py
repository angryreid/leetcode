class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, n = 0, len(arr)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if (j - i + 1) & 1:
                    ans += s
        return ans

"""
For i = 0:

j = 0: Subarray = [1], Length = 1 (odd), Sum = 1, ans = 1
j = 1: Subarray = [1, 2], Length = 2 (even), Sum = 3, ans = 1
j = 2: Subarray = [1, 2, 3], Length = 3 (odd), Sum = 6, ans = 7
For i = 1:

j = 1: Subarray = [2], Length = 1 (odd), Sum = 2, ans = 9
j = 2: Subarray = [2, 3], Length = 2 (even), Sum = 5, ans = 9
For i = 2:

j = 2: Subarray = [3], Length = 1 (odd), Sum = 3, ans = 12

"""