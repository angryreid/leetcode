class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_large_num_map = {}  # 字典，用于存储 nums2 中每个元素的下一个更大元素
        ans = []  # 列表，用于存储 nums1 中每个元素对应的下一个更大元素
        stack = []  # 栈，用于在遍历 nums2 时存储还没有找到下一个更大元素的元素

        for num in reversed(nums2):  # 逆序遍历 nums2
            while stack and num > stack[-1]:  # 弹出栈中所有小于等于 num 的元素
                stack.pop()
            first_large_num_map[num] = stack[-1] if stack else -1  # 栈顶元素是 num 的下一个更大元素，否则为 -1
            stack.append(num)  # 将 num 压入栈中

        for num in nums1:  # 遍历 nums1
            ans.append(first_large_num_map[num])  # 获取 num 对应的下一个更大元素，并添加到结果列表中
        return ans  # 返回结果列表
        # 这个单调栈是递减的，因为在遍历过程中，栈中元素从栈底到栈顶是递减的。当遇到一个更大的元素时，会弹出所有比这个元素小的元素，确保栈顶元素始终是当前元素右侧第一个比它大的元素。