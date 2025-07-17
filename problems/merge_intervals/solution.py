class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key = lambda x: x[0])
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            cur = merged[-1]
            if cur[1] >= intervals[i][0]:
                cur[1] = max(cur[1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged