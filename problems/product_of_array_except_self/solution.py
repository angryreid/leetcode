class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        left_product = [1] * lens
        right_product = [1] * lens
        ans = [0] * lens

        for i in range(1, lens):
            left_product[i] = left_product[i - 1] * nums[i - 1]
            right_product[lens - i - 1] = right_product[lens - i] * nums[lens - i]

        for i in range(lens):
            ans[i] = left_product[i] * right_product[i]

        return ans
        