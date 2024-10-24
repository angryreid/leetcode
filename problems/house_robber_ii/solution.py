class Solution:
    def rob(self, nums):
        # 获取房间总数
        n = len(nums)

        # 如果数组为空，返回0
        if n == 0:
            return 0

        # 如果数组只有一个元素，返回该元素的金额
        if n == 1:
            return nums[0]

        # 不选择第一个房间
        nums_except_first_room = nums[1:]

        # 不选择最后一个房间
        nums_except_last_room = nums[:-1]

        # 从这两个选择中挑选出最大值
        return max(self.myRob(nums_except_first_room), self.myRob(nums_except_last_room))

    def myRob(self, nums):
        # 获取房间总数
        n = len(nums)

        # 创建一个数组value来存放前n个房间可以偷取的最大金额
        value = [0] * (n + 1)

        # 前0个房间无法偷取，金额为0

        # 前1个房间只有一个房间可偷取，金额为该房间的金额
        value[1] = nums[0]

        # 从i = 2到i = n，value中的结果由前i-2和i-1共同决定
        for i in range(2, n + 1):
            # 转移方程：value[i]等于value[i-1]和value[i-2]+nums[i-1]中的较大值
            value[i] = max(value[i - 1], value[i - 2] + nums[i - 1])

        # 返回value的最后一个值
        return value[n]