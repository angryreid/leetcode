class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_large_num_map = {}
        ans = []
        stack = []

        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            first_large_num_map[num] = stack[-1] if stack else -1
            stack.append(num)

        for num in nums1:
            ans.append(first_large_num_map[num])
        return ans
        