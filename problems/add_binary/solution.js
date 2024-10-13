/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let ans = ''
    let carry = 0
    const lenA = a.length - 1
    const lenB = b.length - 1
    let i = 0
    while (i <= lenA || i <= lenB) {
        sum = Number(a[lenA - i] ?? 0) + Number(b[lenB - i] ?? 0) + carry
        ans += sum % 2
        carry = sum >> 1
        i++
    }

    if (carry == 1) {
        ans += '1'
    }

    return ans.split('').reverse().join('')
};