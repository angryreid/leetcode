/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let ans = 0
    const n = heights.length
    let newHeights = new Array(n + 2).fill(0)
    for (let i = 1; i < n + 1; i++) {
        newHeights[i] = heights[i - 1]
    }
    let stack = []
    for (let i = 0; i < n + 2; i++) {
        while(stack.length > 0 && newHeights[i] < newHeights[stack[stack.length - 1]]) {
            const top = stack.pop()
            const height = newHeights[top]
            const left = stack[stack.length - 1]
            const width = i - left - 1
            ans = Math.max(ans, height * width)
        }
        stack.push(i)
    }
    return ans
};