class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt, ans = 0, 0
        for num in nums:
            if cnt == 0:
                ans = num
            if num == ans:
                cnt += 1
            else:
                cnt -= 1

        return ans