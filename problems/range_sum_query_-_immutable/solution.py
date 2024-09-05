class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        sums = self.sums
        for num in nums:
            sums.append(sums[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        sums = self.sums
        return sums[right + 1] - sums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)