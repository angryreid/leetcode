class Solution:
    def evalute(self, num1, num2, op) -> int:
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return int(num1 / num2)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.evalute(num1, num2, token))
        return stack[0]
        