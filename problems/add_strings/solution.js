/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function(num1, num2) {
    let l1 = num1.length - 1
    let l2 = num2.length - 1
    let carry = 0
    res = ''
    while (l1 >= 0 || l2 >= 0) {
        
        x = l1 >= 0 ? Number(num1[l1]) : 0
        y = l2 >= 0 ? Number(num2[l2]) : 0
        total = x + y + carry
        carry = parseInt(total / 10)
        const digit = total % 10
        res = digit + res
        l1 -= 1
        l2 -= 1
    }
    if (carry !== 0) {
        res = carry + res
    }
    return res
};