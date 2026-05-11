"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        if len(s) == 1:
            return s

        result = ""

        for i in range(len(s) - 1):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i + 1)

            if len(odd) > len(result):
                result = odd

            if len(even) > len(result):
                result = even

        return result


    def expand(self, s:str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1 : right]