class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        for i in range(len(intervals)):
            left = intervals[i][0]
            right = intervals[i][1]

            if not res:
                res.append(intervals[i])
                continue

            last = res[-1]
            if last[1] < left:
                res.append(intervals[i])
            else:
                new_right = max(last[1], right)
                res[-1][1] = new_right
        return res
