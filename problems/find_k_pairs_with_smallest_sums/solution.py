class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        ans = []
        while pq and len(ans) < k:
            _, index1, index2 = heappop(pq)
            ans.append([nums1[index1], nums2[index2]])
            index2 += 1
            if index2 < n:
                heappush(pq, (nums1[index1] + nums2[index2], index1, index2))
        return ans
        