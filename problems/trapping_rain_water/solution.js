/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const len = height.length
    let ans = 0
    if (len < 2) return ans
    let stack = []
    for(let i = 0; i < len; i++) {
        while(stack.length > 0 && height[i] > height[stack[stack.length - 1]]) {
            const top = stack[stack.length - 1]
            while(stack.length > 0 && height[top] == height[stack[stack.length - 1]]) {
                stack.pop()
            }
            if (stack.length > 0) {
                left = stack[stack.length - 1]
                ans += (Math.min(height[left], height[i]) - height[top]) * (i - left -1)
            }
        }
        stack.push(i)
    }
    return ans
};