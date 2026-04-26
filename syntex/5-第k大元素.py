"""
5 · 第k大元素
描述
在数组中找到第 k 大的元素。

样例 1：
输入：k = 1, nums = [1,3,4,2]
输出：4

样例 2：
输入：k = 2, nums = [1,3,4,2]
输出：3
"""
from typing import (
    List,
)

class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        # write your code here
        nums.sort(reverse=True)
        return nums[k-1]