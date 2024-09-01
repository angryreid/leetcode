/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    const n = temperatures.length
    let ans = new Array(n).fill(0)
    let stack = []
    const stackTop = () => stack[stack.length - 1] // get the stack top more elegent
    for (let i = 0; i < n; i++){
        while (stack.length > 0 && temperatures[i] > temperatures[stackTop()]) {
            const top = stack.pop()
            ans[top] = i - top // no need to minus 1
        }
        stack.push(i)
    }
    return ans
};