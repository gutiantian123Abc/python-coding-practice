"""
1281 · 前K个高频元素
描述
给定一个非空的整数数组，返回其中出现频率前
k 高的元素。

样例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

样例 2:
输入: nums = [1], k = 1
输出: [1]
"""

from typing import (
    List,
)
import heapq

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
             we will sort your return value in output
    """
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for freq, num in heap:
            res.append(num)

        return res