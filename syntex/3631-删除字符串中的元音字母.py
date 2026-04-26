"""
3631 · 删除字符串中的元音字母
描述
写一个方法，接受给定字符串 s 作为输入，删除字符串中的所有元音字母 a, e, i, o, u，并返回新字符串。

样例 1：
输入：
s = "lintcode"
输出：
"lntcd"

样例 2：
输入：
s = "hello"
输出：
"hll"
"""
class Solution:
    """
    @param s: The string before remove vowels
    @return: The string after remove vowels
    """
    def remove_vowels(self, s: str) -> str:
        # write your code here
        return ''.join(char for char in s if char not in 'aeiou')