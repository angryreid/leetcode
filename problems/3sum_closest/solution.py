class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if abs(target - sum) < abs(target - ans):
                    ans = sum
                
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return sum

                # while left < right and nums[left] == nums[left + 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1
        return ans