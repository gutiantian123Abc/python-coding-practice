"""
437 · 书籍复印
描述
给定n本书，第i本书有pages[i]页。有k个人来抄这些书。
这些书排成一行，每个人都可以索取连续一段的书。
例如，一个抄书人可以连续地将书从第i册复制到第j册，但是他不能复制第1册、第2册和第4册（没有第3册）。
他们在同一时间开始抄书，每抄一页书都要花1分钟。
为了让最慢的抄书人能在最早的时间完成书的分配，最好的策略是什么？
请返回最慢抄书人花费的最短时间。

样例 1:
输入: pages = [3, 2, 4], k = 2
输出: 5
解释: 第一个人复印前两本书, 耗时 5 分钟. 第二个人复印第三本书, 耗时 4 分钟.

样例 2:
输入: pages = [3, 2, 4], k = 3
输出: 4
解释: 三个人各复印一本书.
"""

from typing import (
    List,
)

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    """
    n * log(sum(pages))
    """
    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if not pages:
            return 0

        start, end = max(pages), sum(pages)
        # O(log(sum(pages)))
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people_with_page_limit_per_person(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.get_least_people_with_page_limit_per_person(pages, start) <= k:
            return start

        return end

    # log(n)
    def get_least_people_with_page_limit_per_person(self, pages, page_limit_per_person):
        people_count = 1
        current_pages = 0

        for page in pages:
            if current_pages + page <= page_limit_per_person:
                current_pages += page
            else:
                current_pages = page
                people_count += 1

        return people_count