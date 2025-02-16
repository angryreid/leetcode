class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        self.quickSort(strs, 0, len(strs) - 1)
        # strs.reverse()
        return ''.join(strs) if strs[0] != '0' else '0'

    def quickSort(self, strs: List[str], left: int, right: int):
        if left >= right:
            return

        mid = self.partition(strs, left, right)
        self.quickSort(strs, left, mid - 1)
        self.quickSort(strs, mid + 1, right)

    def partition(self, strs: List[str], left: int, right: int) -> int:
        pivot = strs[left]
        while left < right:
            while left < right and pivot + strs[right] >= strs[right] + pivot:
                right -= 1
            strs[left] = strs[right]

            while left < right and strs[left] + pivot >= pivot + strs[left]:
                left += 1
            strs[right] = strs[left]
        strs[left] = pivot
        return left

