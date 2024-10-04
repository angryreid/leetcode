class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])
        arrow = points[0][1]
        res = 1
        for balloon in points:
            if balloon[0] > arrow:
                arrow = balloon[1]
                res += 1
        return res
        