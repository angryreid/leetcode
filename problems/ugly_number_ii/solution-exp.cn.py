class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 对任意一个丑数来说，乘以 2、3、5 分别可以得到 3 个丑数
        # 因此，对于每一个丑数都乘以 2、3、5，并对结果进行排序即可
        # 因此，2、3、5 就是我们需要处理的质因数
        factors = [2, 3, 5]

        # 由于一些丑数和 2、3、5 相乘会出现重复元素的情况
        # 比如丑数 2 和 2、3、5 相乘得到了 4、【6】、10
        # 而丑数 3 和 2、3、5 相乘得到了【6】、9、15
        # 其中【6】重复了，所以需要去重操作
        # 由于题目说明 n 最大为 1690，会导致丑数的范围超过 int 范围，所以使用 long 来保存

        # 使用优先队列来获取每次集合中最小的数字
        seen = {1}  # 集合中第一个数字是 1

        # 优先队列里面的元素来源于 seen 集合
        pq = [1]

        # 开始不断地迭代丑数的值，直到迭代了 n 次为止
        # 第一个丑数是 1
        for i in range(n - 1):
            # 下一个丑数来源于优先队列的队头元素
            curr = heapq.heappop(pq)

            # 生成新的丑数并加入优先队列
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(pq, nxt)

        # 返回结果
        return heapq.heappop(pq)