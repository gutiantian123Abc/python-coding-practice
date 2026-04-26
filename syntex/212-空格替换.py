"""
212 · 空格替换
描述
设计一种方法，将一个字符串中的所有空格替换成 %20 。字符串以字符数组的形式给出，
你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。

你的程序还需要返回被替换后的字符串的长度。

样例 1：
输入：string[] = "Mr John Smith" and length = 13
输出：string[] = "Mr%20John%20Smith" and return 17
解释：
对于字符串 "Mr John Smith"，长度为 13。替换空格之后，
参数中的字符串需要变为 "Mr%20John%20Smith"，并且把新长度 17 作为结果返回。


样例 2：
输入：string[] = "LintCode and Jiuzhang" and length = 21
输出：string[] = "LintCode%20and%20Jiuzhang" and return 25
解释：
对于字符串 "LintCode and Jiuzhang"，长度为 21。替换空格之后，
参数中的字符串需要变为 "LintCode%20and%20Jiuzhang"，并且把新长度 25 作为结果返回。
"""

class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        if string is None:
            return 0

        new_char_array = ''.join(string[:length]).replace(" ", "%20")
        for i in range(len(new_char_array)):
            string[i] = new_char_array[i]

        return len(string)