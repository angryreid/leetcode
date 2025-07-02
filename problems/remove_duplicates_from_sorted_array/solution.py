class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0                  # 慢指针，指向下一个待填充的位置
        step = 1                   # 控制每个元素最多出现的次数
        for fast in range(len(nums)):  # 快指针遍历整个数组
            if slow < step or nums[fast] != nums[slow - step]:
                nums[slow] = nums[fast]
                slow += 1
        return slow