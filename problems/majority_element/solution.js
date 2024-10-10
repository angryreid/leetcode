/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    cnt = 0
    boss = 0
    for (let num of nums) {
        if (cnt == 0) {
            boss = num
        }

        if (boss == num) {
            cnt++
        } else {
            cnt--
        }
    }
    return boss
};