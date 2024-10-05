class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 题目存在多组解，每一组解都是一个数组，所以使用二维数组存储所有的解
        ans = []

        # 边界情况判断
        if nums == None or len(nums) < 4 :
           return ans

        # 先将数组进行排序操作，从小到大
        nums.sort()

        # 获取数组的长度
        length = len(nums)

        # 开始遍历整个数组
        # 在遍历的过程中，观察设置的四个位置的元素之后的大小
        # 1、第一层循环
        # nums[i] 作为四个元素当中最小的那个元素
        # 需要留下 nums[length - 3] 、nums[length - 2] 、nums[length - 1] 这三个元素
        # 所以 i 的范围是 [ 0  , length - 4 ]
        for i in range(length - 3) : # range is not including length - 3

            # 答案中不可以包含重复的四元组，所以需要执行一个去重的操作
            if i > 0 and nums[i] == nums[i - 1]:
                continue


            # 如果发现当前区间中，最小的四个元素之和都大于了 target
            # 此时，剩下的三个数无论取什么值，四数之和一定大于 target，可以直接退出第一层循环
            if  nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            
            
            # 如果发现当前区间中，选择最大的三个数和 nums[i] 相加都小于了 target
            # 说明此时剩下的三个数无论取什么值，四数之和一定小于 target
            # 因此第一层循环直接进入下一轮，即执行 i++
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target :
                continue
        

            # 来到这里时，通过第一层循环，已经确定 nums[i] 这个数
            # 在 [ i + 1 , length - 1 ] 这个区间中寻找剩下的两个数
            # 2、第二层循环
            # nums[j] 作为四个元素当中第二小的那个元素
            # 需要留下 nums[length - 2] 、nums[length - 1] 这三个元素
            # 所以 j 的范围是 [ i + 1  , length - 3 ]
            for j in range( i + 1,length - 2) :

                # 答案中不可以包含重复的四元组，所以需要执行一个去重的操作
                if j > i + 1 and nums[j] == nums[j - 1] :
                    continue
                

                # 如果发现当前区间中，最小的四个元素之和都大于了 target
                # 此时，剩下的三个数无论取什么值，四数之和一定大于 target，可以直接退出第二层循环 
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target :
                    break
            

                # 如果发现当前区间中，选择最大的三个数和 nums[i] 相加都小于了 target
                # 说明此时剩下的三个数无论取什么值，四数之和一定小于 target
                # 因此第二层循环直接进入下一轮，即执行 j++
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
            

                # 否则的话，开始去寻找剩下的两个数
                #  在 [ j + 1 , length - 1 ] 这个区间
                left = j + 1 

                right = length - 1

                # left 和 right 不断的向内移动
                # 逻辑和三数之和的逻辑一样
                while left < right :

                    # 计算这四个元素之和
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    # 发现四者之和为 0
                    if sum == target :
                        # 把这个结果记录一下
                        ans.append([nums[i], nums[j],nums[left],nums[right]])

                        # 答案中不可以包含重复的三元组，所以需要执行一个去重的操作
                        # 比如这个输入 [-2,0,0,2,2]
                        # i 指向的元素值为 -2 ，left 指向的元素值为第一个 0 ，right 指向的元素值为倒数第一个 2 时
                        # 它们的 sum 为 0 ，如果让 ，left 向右移动一下，，right 向左移动一下，它们的 sum 也为 0
                        # 但是这两组解都是 [ -2 , 0 , 2]，所以需要去重
                        while left < right and nums[left] == nums[left + 1] :
                            # left 向右移动
                            left += 1


                        while left < right and nums[right] == nums[right - 1] :
                            # right 向左移动
                            right -= 1
                        

                        # left 向右移动
                        left += 1

                        # right 向左移动
                        right -= 1

                    # 如果四者之和小于 0 ，那么说明需要找更大的数
                    elif sum < target :
                        # left 向右移动
                        left += 1

                    # 如果四者之和大于 0 ，那么说明需要找更小的数
                    else :
                        # right 向左移动
                        right -= 1
        # 返回结果
        return ans