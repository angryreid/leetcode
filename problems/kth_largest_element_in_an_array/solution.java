// 登录 AlgoMooc 官网获取更多算法图解
// https://www.algomooc.com
// 作者：程序员吴师兄
// 代码有看不懂的地方一定要私聊咨询吴师兄呀
// https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
class Solution {
     public int findKthLargest(int[] nums, int k) {
        // 执行快速排序操作，定位找到下标为 k - 1 的那个元素
        int[] res = quickSort(nums,0,nums.length - 1,k - 1);

        return res[k-1];
    }


    // 函数传入待排序数组 nums
    // 排序区间的左端点 left
    // 排序区间的右端点 right
    private int[] quickSort(int[] nums,int left, int right , int index){

        // 调用函数 partition，将 left 和 right 之间的元素划分为左右两部分
        int mid = partition(nums,left,right);

        // 如果 mid 下标恰巧为 index，那么找到了最小的 k 个数
        if (mid == index) {
            // 直接返回
            return Arrays.copyOf(nums, mid + 1);

        // 如果 mid 下标大于 index，那么说明需要在左侧元素中去切分
        }else if( mid > index ){

            // 对 mid 左侧的元素进行快速排序
            return quickSort(nums,left,mid - 1, index );
        }else{

            // 对 mid 右侧的元素进行快速排序
            return quickSort(nums,mid + 1,right, index );
        }

    }

    private int partition(int[] nums, int left ,int right){

        // 经典快速排序的写法
        // 设置当前区间的第一个元素为基准元素
        int pivot = nums[left];

        // left 向右移动，right 向左移动，直到 left 和 right 指向同一元素为止
        while( left < right ){

            // 只有当遇到小于 pivot 的元素时，right 才停止移动
            // 此时，right 指向了一个小于 pivot 的元素，这个元素不在它该在的位置上
            while( left < right && nums[right] <= pivot ){
                // 如果 right 指向的元素是大于 pivot 的，那么
                // right 不断的向左移动
                right--;
            }

            // 将此时的 nums[left] 赋值为 nums[right]
            // 执行完这个操作，比 pivot 小的这个元素被移动到了左侧
            nums[left] = nums[right];


            // 只有当遇到大于 pivot left 才停止移动
            // 此时，left 指向了一个大于 pivot 的元素，这个元素不在它该在的位置上
            while( left < right && nums[left] >= pivot){
                // 如果 left 指向的元素是小于 pivot 的，那么
                // left 不断的向右移动
                left++;
            }

            // 将此时的 nums[right] 赋值为 nums[left]
            // 执行完这个操作，比 pivot 大的这个元素被移动到了右侧
            nums[right] = nums[left];

        }

        // 此时，left 和 right 相遇，那么需要将此时的元素设置为 pivot
        // 这个时候，pivot 的左侧元素都小于它，右侧元素都大于它
        nums[left] = pivot;

        // 返回 left
        return left;

    }
}