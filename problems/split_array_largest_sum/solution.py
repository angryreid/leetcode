class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        for num in nums:
            left = max(left, num)
            right += num
            while left <= right:
                mid = left + (right - left) // 2
                cnt = self.subSplit(nums, mid)
                if cnt > k:
                    left = mid + 1
                elif cnt < k:
                    right = mid - 1
                else:
                    right = mid - 1
        return left
    
    def subSplit(self, nums: List[int], max_sum: int) -> int:
        cnt = 1
        temp_sum = 0
        for num in nums:
            if temp_sum + num > max_sum:
                cnt += 1
                temp_sum = 0
            temp_sum += num
        return cnt