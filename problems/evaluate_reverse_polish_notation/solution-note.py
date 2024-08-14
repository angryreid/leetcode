class Solution:
    # Method to evaluate a simple expression with two operands and an operator
    def evaluate(self, num1, num2, op) -> int:
        if op == "+":  # If the operator is addition
            return num1 + num2
        elif op == "-":  # If the operator is subtraction
            return num1 - num2
        elif op == "*":  # If the operator is multiplication
            return num1 * num2
        elif op == "/":  # If the operator is division
            return int(num1 / num2)  # Perform integer division

    # Method to evaluate an expression in Reverse Polish Notation
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize an empty stack
        for token in tokens:  # Iterate over each token in the input list
            try:
                stack.append(int(token))  # Try to convert the token to an integer and push it onto the stack
            except:  # If the token is not an integer (i.e., it's an operator)
                num2 = stack.pop()  # Pop the top two elements from the stack
                num1 = stack.pop()
                stack.append(self.evaluate(num1, num2, token))  # Evaluate the expression and push the result back onto the stack
        return stack[0]  # The final result will be the only element left in the stack