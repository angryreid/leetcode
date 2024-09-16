class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pre = 0
        pre_sum_map = collections.defaultdict(int)
        pre_sum_map[0] = 1
        for num in nums:
            pre += num
            cnt += pre_sum_map[pre - k]
            pre_sum_map[pre] += 1
        return cnt

        