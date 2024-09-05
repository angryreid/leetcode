class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans, n = 0, len(arr)  # 初始化结果变量 ans 为 0，数组长度 n 为 arr 的长度
        for i in range(n):  # 遍历数组的每个起始位置 i
            s = 0  # 初始化子数组和 s 为 0
            for j in range(i, n):  # 从起始位置 i 遍历到数组末尾位置 j
                s += arr[j]  # 将当前元素 arr[j] 加到子数组和 s 中
                if (j - i + 1) & 1:  # 如果子数组的长度是奇数
                    ans += s  # 将子数组和 s 加到结果 ans 中
        return ans  # 返回所有奇数长度子数组的和