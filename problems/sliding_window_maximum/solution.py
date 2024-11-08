class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k <= 1:
            return nums
        n = len(nums)
        res = []
        q = collections.deque()
        for i in range(k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])

        for i in range(k, n):
            if q[0] == nums[i - k]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

            res.append(q[0])
        return res
