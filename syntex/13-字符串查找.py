"""
13 · 字符串查找

描述：
    对于一个给定的 source 字符串和一个 target 字符串，
    在 source 字符串中找出 target 字符串出现的第一个位置（从0开始）。
    如果不存在，则返回 -1。

样例 1：
    输入：source = "source", target = "target"
    输出：-1
    解释：source 中不包含 target，返回 -1

样例 2：
    输入：source = "abcdabcdefg", target = "bcd"
    输出：1
    解释：target 在 source 中第一次出现的位置是下标 1

样例 3：
    输入：source = "lintcode", target = ""
    输出：0
    解释：target 为空字符串时，返回 0
"""

class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        # Write your code here
        return source.find(target)
