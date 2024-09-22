class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        prefix_sum = 0
        max_interval = 0
        prefix_map = {}
        for i, value in enumerate(hours):
            prefix_sum += 1 if value > 8 else -1
            if prefix_sum > 0:
                max_interval = i + 1
            else:
                if prefix_sum - 1 in prefix_map:
                    max_interval = max(max_interval, i - prefix_map[prefix_sum - 1])
                if prefix_sum not in prefix_map:
                    prefix_map[prefix_sum] = i

        return max_interval
        