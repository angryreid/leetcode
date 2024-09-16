class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostOddIn(k):
            ans = cnt = left = 0
            for right in range(len(nums)):
                cnt += nums[right] % 2
                while cnt > k:
                    cnt -= nums[left] % 2
                    left += 1
                ans += right - left + 1
            return ans
        return atMostOddIn(k) - atMostOddIn(k - 1)
        