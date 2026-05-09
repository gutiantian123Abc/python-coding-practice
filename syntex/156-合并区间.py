"""
156 · 合并区间

描述
我们以一个 Interval 类型的列表 intervals 来表示若干个区间的集合，其中单个区间为 (start, end)。
你需要合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

你需要对有重叠部分的区间进行合并
即使某个区间与其他区间都没有重叠，也需要将其输出

样例1:
输入: [(1,3)]
输出: [(1,3)]

样例 2:
输入:  [(1,3),(2,6),(8,10),(15,18)]
输出: [(1,6),(8,10),(15,18)]
"""
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # write your code here
        intervals = sorted(intervals, key=lambda x : x.start)
        result = []

        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)

        return result