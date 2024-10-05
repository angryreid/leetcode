class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        target = 0
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] > target:
                break

            if nums[i] + nums[n - 2] + nums[n - 1] < target:
                continue
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return ans
        