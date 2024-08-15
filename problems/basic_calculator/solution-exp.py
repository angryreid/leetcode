class Solution:
    def calculate(self, s: str) -> int:
        stack = list()  # Initialize an empty stack to keep track of results and signs
        sign = 1  # Initialize the sign as positive
        res = 0  # Initialize the result as 0
        length = len(s)  # Get the length of the input string
        i = 0  # Initialize the index to 0
        while i < length:  # Iterate over each character in the string
            ch = s[i]  # Get the current character
            if ch == ' ':  # If the character is a space, skip it
                i += 1
            elif ch.isdigit():  # If the character is a digit
                value = ord(s[i]) - ord('0')  # Convert the character to an integer
                while i + 1 < length and s[i + 1].isdigit():  # Check for multi-digit numbers
                    i += 1
                    value = value * 10 + ord(s[i]) - ord('0')  # Update the value
                res += value * sign  # Add the value to the result with the correct sign
                i += 1
            elif ch == '+':  # If the character is a plus sign
                sign = 1  # Set the sign to positive
                i += 1
            elif ch == '-':  # If the character is a minus sign
                sign = -1  # Set the sign to negative
                i += 1
            elif ch == '(':  # If the character is an opening parenthesis
                stack.append(res)  # Push the current result onto the stack
                res = 0  # Reset the result
                stack.append(sign)  # Push the current sign onto the stack
                sign = 1  # Reset the sign to positive
                i += 1
            elif ch == ')':  # If the character is a closing parenthesis
                formerSign = stack.pop()  # Pop the sign from the stack
                formerRes = stack.pop()  # Pop the result from the stack
                res = formerRes + formerSign * res  # Update the result with the popped values
                i += 1
        return res  # Return the final result