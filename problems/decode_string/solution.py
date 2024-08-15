class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        digit = 0
        numStack = []
        strStack = []
        for ch in s:
            if '0' <= ch <= '9':
                num = int(ch)
                digit = digit * 10 + num
            elif 'a' <= ch <= 'z':
                res += ch
            elif ch == "[":
                numStack.append(digit)
                strStack.append(res)
                digit = 0
                res = ""
            elif ch == "]":
                count = numStack.pop()
                outterStr = strStack.pop()
                for i in range(count):
                    outterStr += res
                res = outterStr
        return res

        