class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_large_num_map = {}  # Dictionary to store the next greater element for each number in nums2
        ans = []  # List to store the results for nums1
        stack = []  # Stack to keep track of the elements for which we are finding the next greater element

        for num in reversed(nums2):  # Iterate through nums2 in reverse order
            while stack and num > stack[-1]:  # Pop elements from the stack that are smaller than the current number
                stack.pop()
            first_large_num_map[num] = stack[-1] if stack else -1  # The next greater element is the top of the stack, or -1 if the stack is empty
            stack.append(num)  # Push the current number onto the stack

        for num in nums1:  # Iterate through nums1
            ans.append(first_large_num_map[num])  # Append the next greater element for each number in nums1 to the result list
        return ans  # Return the result list