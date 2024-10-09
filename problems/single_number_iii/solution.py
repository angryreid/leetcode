class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            return nums

        xor = 0
        for num in nums:
            xor ^= num
        
        set_bit = xor & -xor

        a, b = 0, 0
        for num in nums:
            if num & set_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]