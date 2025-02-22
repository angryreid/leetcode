class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=[i for i in range(1,n+1)]
        c=combinations(l,k)
        p=[list(i)for i in list(c)]
        return (p)
        