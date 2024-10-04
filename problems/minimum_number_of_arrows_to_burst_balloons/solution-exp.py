class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])  # 按气球的右边界进行排序
        arrow = points[0][1]  # 初始化第一个箭的位置为第一个气球的右边界
        res = 1  # 初始化箭的数量为1
        for balloon in points:  # 遍历所有气球
            if balloon[0] > arrow:  # 如果当前气球的左边界在箭的右边，则需要一支新的箭
                arrow = balloon[1]  # 更新箭的位置为当前气球的右边界
                res += 1  # 箭的数量加1
        return res  # 返回所需的最少箭的数量