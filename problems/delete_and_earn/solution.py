from collections import deque, defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 统计每个数字的总点数
        points = defaultdict(int)
        for num in nums:
            points[num] += num

        # 获取所有独特的数字并排序
        unique_nums = sorted(points.keys())

        # 使用缓存来存储已经计算过的结果
        memo = {}

        def dfs(index):
            if index >= len(unique_nums):
                return 0
            if index in memo:
                return memo[index]

            # 选择当前数字
            take = points[unique_nums[index]]
            next_index = index + 1
            while next_index < len(unique_nums) and unique_nums[next_index] == unique_nums[index] + 1:
                next_index += 1
            take += dfs(next_index)

            # 不选择当前数字
            skip = dfs(index + 1)

            # 取最大值
            result = max(take, skip)
            memo[index] = result
            return result

        return dfs(0)

        