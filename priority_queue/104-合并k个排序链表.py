"""
104 · 合并k个排序链表
描述
合并 k 个排序链表（序列为升序序列），并且返回合并后的排序链表（序列为升序序列）。尝试分析和描述其复杂度。

样例 1：
输入：
lists = [2->4->null,null,-1->null]
输出：
-1->2->4->null
解释：
将2->4->null、null和-1->null合并成一个升序的链表。

样例 2：
输入：
lists = [2->6->null,5->null,7->null]
输出：
2->5->6->7->null
解释：
将2->6->null、5->null和7->null合并成一个升序的链表。
"""
import heapq
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next