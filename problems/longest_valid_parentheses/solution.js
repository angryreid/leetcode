/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    max = 0
    stack = []
    start = 0
    len = s.length
    for(let i = 0; i < len; i++) {
        if (s[i] == '(') {
            stack.push(i)
        } else {
            if (stack.length == 0) {
                start = i + 1
            } else {
                stack.pop()
                if (stack.length == 0) {
                    max = Math.max(max, i - start + 1)
                } else {
                    max = Math.max(max, i - (stack[stack.length - 1] + 1) + 1)
                }
            }
        }
    }
    return max
};