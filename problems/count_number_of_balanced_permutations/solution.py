class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # Calculate the number of even and odd positions in the string
        even, odd = len(num) // 2, len(num) - len(num) // 2
        # Count the occurrences of each digit in the string
        cnt = Counter(int(ch) for ch in num)
        # Calculate the total sum of all digits in the string
        total = sum(int(ch) for ch in num)

        @cache
        def dfs(i, odd, even, balanced_sum):
            # Base case: if no odd or even positions left and balanced_sum is zero, return 1
            if odd == 0 and even == 0 and balanced_sum == 0:
                return 1
            # If index exceeds 9 or any of the counts are negative, return 0
            if i > 9 or odd < 0 or even < 0 or balanced_sum < 0:
                return 0
            res = 0
            # Iterate through all possible counts of the current digit
            for j in range(0, cnt[i] + 1):
                # Calculate the number of ways to distribute the current digit
                res += comb(odd, j) * comb(even, cnt[i] - j) * dfs(i + 1, odd - j, even - cnt[i] + j, balanced_sum - i * j)
            # Return the result modulo 1000000007
            return res % 1000000007

        # If the total sum is odd, return 0, otherwise start the DFS
        return 0 if total % 2 else dfs(0, odd, even, total // 2)  