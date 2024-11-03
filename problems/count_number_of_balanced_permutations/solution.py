class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        even, odd = len(num) // 2, len(num) - len(num) // 2
        cnt = Counter(int(ch) for ch in num)
        total = sum(int(ch) for ch in num)

        @cache
        def dfs(i, odd, even, balanced_sum):
            if odd == 0 and even == 0 and balanced_sum == 0:
                return 1
            if i > 9 or odd < 0 or even < 0 or balanced_sum < 0:
                return 0
            res = 0
            for j in range(0, cnt[i] + 1):
                res += comb(odd, j) * comb(even, cnt[i] - j) * dfs(i + 1, odd - j, even - cnt[i] + j, balanced_sum - i * j)
            return res % 1000000007

        return 0 if total % 2 else dfs(0, odd, even, total // 2)  