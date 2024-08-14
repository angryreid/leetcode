class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        stack = list()
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == '[':
                stack.append(c)
            elif c == '{':
                stack.append(c)
            else:
                if not stack: # empty stack
                    return False
                
                top = stack[-1]
                if (top == '(' and c == ')') or (top == '[' and c == ']') or (top == '{' and c == '}'):
                    stack.pop()
                else:
                    return False
        return not stack # empty stack
        