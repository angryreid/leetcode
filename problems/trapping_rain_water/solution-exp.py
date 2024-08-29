class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)  # Get the number of elements in the height list
        ans = 0  # Initialize the answer to 0
        if n < 2:  # If there are less than 2 elements, no water can be trapped
            return ans
        stack = []  # Initialize an empty stack to keep track of indices
        for i in range(n):  # Iterate over each element in the height list
            while stack and height[i] > height[stack[-1]]:  # While the stack is not empty and the current height is greater than the height at the top of the stack
                top = stack.pop()  # Pop the top element from the stack
                while stack and height[top] == height[stack[-1]]:  # Remove all elements with the same height as the popped element
                    stack.pop()
                if stack:  # If the stack is not empty
                    left = stack[-1]  # Get the index of the left boundary
                    ans += (min(height[left], height[i]) - height[top]) * (i - left - 1)  # Calculate the trapped water and add it to the answer
            stack.append(i)  # Push the current index onto the stack
        return ans  # Return the total amount of trapped water