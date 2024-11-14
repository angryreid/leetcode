class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 中位数的概念：将一个集合划分为两个长度相等的子集，其中一个子集中的元素总是大于另一个子集中的元素
        # 由于数组的长度有两种情况：奇数、偶数
        # 奇数组: [2 3 5] 对应的中位数为 3
        # 偶数组: [1 4 7 9] 对应的中位数为 ( 4 + 7 ) / 2 = 5.5


        # 获取 nums1 的长度
        n = len(nums1)

        # 获取 nums2 的长度
        m = len(nums2)

        if n > m :
            # 通过这个方法，可以将 nums1 和 nums2 进行一个交换操作，确保 nums1 的长度一定小于 nums2
            return self.findMedianSortedArrays(nums2,nums1)
    

        # nums1、nums2 均为有序数组
        # 如果将有序数组切割分成两部分，那么切的那个位置的左侧为左边最大值，切的那个位置的右侧为右边最小值
        #      |
        # [1 4 | 7 9] 
        #      |
        # 比如 4 就是左部分的最大值，7 就是右部分的最小值

        # 设置两个变量 Cut1、Cut2 方便切割 nums1、nums2
        # 不断的挪动 Cut1 和 Cut2 切的位置，如果说 Cut1、Cut2 找到了合适的位置进行切割
        # 1、 ( nums1 的左部分 + nums2 的左部分 ）个数 = （ nums1 的右部分 + nums2 的右部分 ）个数】
        # 2、( nums1 的左部分 + nums2 的左部分 ）最大数 <= （ nums1 的右部分 + nums2 的右部分 ）最小数
        # 那么也就找到了中位数

        # 一开始 Cut1 为 0
        Cut1 = 0

        # 一开始 Cut2 为 0
        Cut2 = 0

        # nums1、nums2 均为有序数组
        # 显然，LMax1 <= RMin1，LMax2 <= RMin2

        # LMax1 表示 nums1 被 Cut1 切割后，左部分的最大值
        LMax1 = 0

        # LMax2 表示 nums2 被 Cut2 切割后，左部分的最大值
        LMax2 = 0

        # RMin1 表示 nums1 被 Cut1 切割后，右部分的最小值
        RMin1 = 0

        # RMin2 表示 nums2 被 Cut2 切割后，右部分的最小值
        RMin2 = 0

        # 一开始 Cut1 = 0，Cut2 = 0 ，也就是说 nums1 的左部分 0 个元素， nums2 的左部分 0 个元素
        # 因此需要挪动 Cut1、Cut2 的位置，使得 ( nums1 的左部分 + nums2 的左部分 ）个数 = （ nums1 的右部分 + nums2 的右部分 ）个数

        # 所以，一开始直接把 Cut1 挪到 nums1 的中间位置进行切割，把 Cut2 挪到 nums2 的中间位置进行切割
        # 如果 LMax1 <= RMin2，LMax2 <= RMin1
        # 又由于 LMax1 <= RMin1，LMax2 <= RMin2
        # 意味着
        # 1、( nums1 的左部分 + nums2 的左部分 ）个数 = （ nums1 的右部分 + nums2 的右部分 ）个数
        # 2、( nums1 的左部分 + nums2 的左部分 ）最大数 <= （ nums1 的右部分 + nums2 的右部分 ）最小数

        # 当发现 LMax1 > RMin2 时，说明 Cut1 切的位置不对，左边的元素太多了，需要把一些元素挪到右边来，这样才能减小 LMax1 的值
        # 所以  Cut1 的值减小了
        # 而因为 ( nums1 的左部分 + nums2 的左部分 ）个数 = Cut1 + Cut2
        # Cut2 变大了，也就是说可以通过 Cut1 的位置找到 Cut2 的位置

        # 由于 m + n 可能为奇数, 也可能为偶数，为了方便统一处理，这里加入一个技巧
        # 在数组的 开头、结尾、数字直接加入一个 “#”
        # 这样 nums2 的长度 m 变成了 2m + 1
        # 这样 nums1 的长度 n 变成了 2n + 1
        # 两数之和变成了 2m + 2n + 2，恒为偶数
        # 比如 [ 1 、3 、5 、7 ] 变成了 [ #、 1 、# 、3 、 # 、5  、 # 、7 、# ]
        # 比如 [ 2 、4 、6 ] 变成了 [ #、 2 、# 、4 、 # 、6  、 #  ]
        # 因此，每个位置的下标位置发生了改变，但可以通过 /2 得到原来元素的位置：
        # 比如 1，原来在 0 位，现在是 1 位，1 / 2 = 0
        # 比如 3，原来在 1 位，现在是 3 位，3 / 2 = 1
        # 比如 6，原来在 2 位，现在是 5 位，5 / 2 = 2

        # 此时，LMax1 = ( Cut1 - 1 ) / 2 位置上的元素
        # RMin1 = Cut1 / 2 位置上的元素

        # 接下来，开始找 Cut1 和 Cut2 的位置了

        # left 为 nums1 最左侧的元素，可以获取到
        left = 0

        # 添加了 “#” 后，nums1 的长度 n 变成了 2n + 1
        # right 为 nums1 最右侧的元素，可以获取到
        right = 2 * n  

        # 在 while 循环里面，left 不断的 ++，而 right 不断的 --
        # 当 [ left , right ] 这个区间不存在元素的时候，才跳出 while 循环，也就是当 left > right 时跳出循环
        # 即当 left = right + 1 时，搜索区间没有元素了
        # 由于 left 和 right 相遇的时候指向同一个元素，这个元素是存在于 [ left , right] 区间，这个区间就一个元素
        # 所以此时 while 循环的判断可以使用等号
        while left <= right :

            # Cut1 切在 nums1 的中间位置
            Cut1 = left + ( right - left ) // 2

            # ( nums1 的左部分 + nums2 的左部分 ）个数 = m + n
            # 所以 Cut2 = m + n - Cut1
            Cut2 = m + n - Cut1

            # 注意几种边界情况

            # 1、nums1 左部分没有元素，全部都在右部分，并且元素值都比中值大
            # 所以，中值在 nums2 中，这里就可以假定 LMax1 = INT_MIN
            if Cut1 == 0 :
                LMax1 = -1000001
            else :
                # 否则 LMax1 切割位置的左边元素
                LMax1 = nums1[ (Cut1 - 1) // 2 ]
        

            # 2、nums1 右部分没有元素，全部都在左部分，并且元素值都比中值小
            # 所以，中值在 nums2 中，这里就可以假定 RMin1 = MAX_VALUE
            if Cut1 == 2 * n :
                RMin1 = 1000001
            else:
                # 否则 RMin1 切割位置的右边元素
                RMin1 = nums1[ Cut1  // 2 ] 
        

            # 3、nums2 左部分没有元素，全部都在右部分，并且元素值都比中值大
            # 所以，中值在 nums1 中，这里就可以假定 LMax2 = INT_MIN
            if Cut2 == 0 :
                LMax2 = -1000001
            else:
                # 否则 LMax2 切割位置的左边元素
                LMax2 = nums2[ (Cut2 - 1) // 2 ]
        

            # 2、nums2 右部分没有元素，全部都在左部分，并且元素值都比中值小
            # 所以，中值在 nums1 中，这里就可以假定 RMin2 = MAX_VALUE
            if Cut2 == 2 * m :
                RMin2 = 1000001
            else: 
                # 否则 RMin2 切割位置的右边元素
                RMin2 = nums2[ Cut2  // 2 ]
            

            # LMax1 > RMin2
            # 说明 Cut1 切的位置不对，左边的元素太多了，需要把一些元素挪到右边来，这样才能减小 LMax1 
            # Cut1 切的位置向左边挪一些
            if  LMax1 > RMin2 :
                # 也就是说缩小之后的区间最右侧位置为 Cut1 - 1
                right = Cut1 - 1

            # LMax2 > RMin1
            # 说明 Cut1 切的位置不对，左边的元素太少了，需要把一些元素挪到左边来，这样才能增大 RMin1  
            # Cut1 切的位置向右边挪一些
            elif  LMax2 > RMin1 :
                # 也就是说缩小之后的区间最左侧位置为 Cut1 + 1
                left = Cut1 + 1
            else:
                # 否则就是说明切的位置合适，不用再找其它位置了
                # 1、( nums1 的左部分 + nums2 的左部分 ）个数 = （ nums1 的右部分 + nums2 的右部分 ）个数
                # 2、( nums1 的左部分 + nums2 的左部分 ）最大数 <= （ nums1 的右部分 + nums2 的右部分 ）最小数
                break
            
        # 那么再获取 LMax1 和 LMax2 较大值 + RMin1 和 RMin2 的较小值
        # 两者相加除以 2 就是结果
        return (max(LMax1,LMax2) + min(RMin1,RMin2)) / 2.0