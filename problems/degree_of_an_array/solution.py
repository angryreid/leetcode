class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        mp = dict()

        for i, num in enumerate(nums):
            if num in mp:
                mp[num][0] += 1
                mp[num][2] = i
            else:
                mp[num] = [1, i, i]
        
        maxCnt = minLen = 0
        for cnt, left, right in mp.values():
            if maxCnt < cnt:
                maxCnt = cnt
                minLen = right - left + 1
            elif maxCnt == cnt:
                if minLen > (newLen := right - left + 1):
                    minLen = newLen

        return minLen

        