class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # 初始化一个空栈，用于存储最终保留的数字
        for digit in num:  # 遍历输入的每一个数字
            while k and stack and stack[-1] > digit:  # 当需要移除的数字还未达到k，并且栈不为空，且栈顶元素大于当前数字时
                stack.pop()  # 弹出栈顶元素
                k -= 1  # 需要移除的数字数量减1
            stack.append(digit)  # 将当前数字压入栈中
            
        # 拼接栈中的数字，并移除多余的k个数字（如果有），去掉前导零，如果结果为空则返回'0'
        return ''.join(stack[:len(stack) - k]).lstrip('0') or '0'

        # Edge case for ''.join(stack[:len(stack) - k]).lstrip('0') is ''

        '''
        stack = ['1', '2', '3']
        k = 3
        # Slicing the stack
        stack[:len(stack) - k]  # stack[:3 - 3] => stack[:0] => []
        # Joining the elements
        ''.join([])  # ''
        # Stripping leading zeros (no effect here as the string is already empty)
        ''.join([]).lstrip('0')  # ''


        stack = ['0', '0', '0']
        k = 1
        # Slicing the stack
        stack[:len(stack) - k]  # stack[:3 - 1] => stack[:2] => ['0', '0']
        # Joining the elements
        ''.join(['0', '0'])  # '00'
        # Stripping leading zeros
        '00'.lstrip('0')  # ''
        '''