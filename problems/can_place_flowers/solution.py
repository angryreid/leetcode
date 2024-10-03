class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur = 0
        lens = len(flowerbed)
        while cur < lens and n > 0:
            if flowerbed[cur] == 1:
                cur += 2
            elif cur == lens - 1 or flowerbed[cur + 1] == 0:
                cur += 2
                n -= 1
            else:
                cur += 3
        return n <= 0
        