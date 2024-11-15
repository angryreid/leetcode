# Explain

**核心思想：**

该方法的核心在于找到两个数组的正确分割点，使得所有在分割点左边的元素都小于等于所有在分割点右边的元素。如果我们能找到这样的分割点，那么中位数就可以根据分割点附近的元素计算出来。

**步骤详解：**

1. **预处理：**

   * 确保 `nums1` 是较短的数组。如果 `nums1` 比 `nums2` 长，则交换它们。这样做可以简化后续的边界条件处理。
   * 初始化二分查找的边界：`low = 0`，`high = len(nums1)`。  `low` 和 `high` 定义了 `nums1` 中可能的分割点范围。

2. **二分查找循环：**

   * `while low <= high:`  循环继续，直到 `low` 和 `high` 交叉，这意味着我们已经找到了最佳分割点。

3. **计算分割点：**

   * `partition1 = (low + high) // 2`：计算 `nums1` 的分割点。
   * `partition2 = (m + n + 1) // 2 - partition1`：计算 `nums2` 的分割点。这个公式保证了分割点左边的元素总数和右边的元素总数大致相等（或者左边多一个，如果总元素个数是奇数）。

4. **计算分割点附近元素：**

   * `maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]`：`nums1` 左侧的最大值。如果 `partition1` 为 0，则左侧没有元素，使用负无穷作为占位符。
   * `minRight1 = float('inf') if partition1 == n1 else nums1[partition1]`：`nums1` 右侧的最小值。如果 `partition1` 为 `n1`，则右侧没有元素，使用正无穷作为占位符。
   * `maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]`：`nums2` 左侧的最大值。
   * `minRight2 = float('inf') if partition2 == n2 else nums2[partition2]`：`nums2` 右侧的最小值。

5. **检查分割点是否有效：**

   * `if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:`：如果满足这个条件，说明我们找到了正确的分割点。所有左侧元素都小于等于所有右侧元素。

6. **计算中位数：**

   * `if (n1 + n2) % 2 == 0:`：如果总元素个数是偶数，中位数是左右两侧最大值的平均值。
   * `else:`：如果总元素个数是奇数，中位数是左侧的最大值。

7. **调整分割点（如果无效）：**

   * `elif maxLeft1 > minRight2:`：如果 `nums1` 左侧的最大值大于 `nums2` 右侧的最小值，说明 `nums1` 的分割点太靠右了，需要将其左移。`high = partition1 - 1`。
   * `else:`：否则，说明 `nums1` 的分割点太靠左了，需要将其右移。`low = partition1 + 1`。

**示例：**

假设 `nums1 = [1, 3]`，`nums2 = [2]`。

1. `n1 = 2`，`n2 = 1`。
2. `low = 0`，`high = 2`。
3. 第一次循环：`partition1 = 1`，`partition2 = 1`。`maxLeft1 = 1`，`minRight1 = 3`，`maxLeft2 = 2`，`minRight2 = 2`。`maxLeft1 <= minRight2` 成立，但 `maxLeft2 <= minRight1` 也成立。因此，中位数为 `(max(1, 2) + min(3, 2)) / 2 = 2`。

**关键点：**

* 使用负无穷和正无穷作为占位符可以简化边界条件的处理。
* `(m + n + 1) // 2 - partition1` 公式是关键，它确保了分割点的正确性。
* 二分查找的思想可以有效地将时间复杂度降低到对数级别。
