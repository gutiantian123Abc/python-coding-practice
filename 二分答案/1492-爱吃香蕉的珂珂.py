"""
1492 · 爱吃香蕉的珂珂
描述
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。
珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，
从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= piles[i] <= 10^9

样例 1:
输入: piles = [3,6,7,11], H = 8
输出: 4
解释：6->4*2,7->4*2,11->4*3,3->4*1

样例 2:
输入: piles = [30,11,23,4,20], H = 5
输出: 30
解释：4->30*1,11->30*1,20->30*1,23->30*1,30->30*1
"""

from typing import (
    List,
)
import math

class Solution:
    """
    @param piles: an array
    @param h: an integer
    @return: the minimum integer K
    """
    def min_eating_speed(self, piles: List[int], h: int) -> int:
        # Write your code here
        left = 0
        right = max(piles)

        while left + 1 < right:
            mid = (left + right) // 2
            if self.can_finish(piles, h, mid):
                right = mid
            else:
                left = mid

        if left != 0 and self.can_finish(piles, h, left):
            return left

        return right

    def can_finish(self, piles: List[int], h: int, speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/speed)

        return hours <= h