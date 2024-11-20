# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # 如果列表为空，直接返回
            return
        return self.merge(lists, 0, len(lists) - 1)  # 调用 merge 函数合并所有链表
    
    def merge(self, lists, left, right):
        if left == right:  # 如果左右指针相等，返回当前链表
            return lists[left]
        mid = left + (right - left) // 2  # 计算中间位置
        l1 = self.merge(lists, left, mid)  # 递归合并左半部分
        l2 = self.merge(lists, mid + 1, right)  # 递归合并右半部分
        return self.mergeTwoLists(l1, l2)  # 合并左右两部分并返回结果
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()  # 创建一个哑节点
        pre = dummy  # 初始化前驱节点为哑节点

        while l1 and l2:  # 当两个链表都不为空时
            if l1.val < l2.val:  # 如果 l1 的值小于 l2 的值
                pre.next = l1  # 将 l1 连接到前驱节点
                l1 = l1.next  # 移动 l1 到下一个节点
            else:
                pre.next = l2  # 将 l2 连接到前驱节点
                l2 = l2.next  # 移动 l2 到下一个节点
            pre = pre.next  # 移动前驱节点到下一个节点
        
        if l1:  # 如果 l1 不为空
            pre.next = l1  # 将剩余的 l1 连接到前驱节点

        if l2:  # 如果 l2 不为空
            pre.next = l2  # 将剩余的 l2 连接到前驱节点
        
        return dummy.next  # 返回合并后的链表头节点