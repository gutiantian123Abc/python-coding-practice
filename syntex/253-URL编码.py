"""
253 · URL 编码

描述：
    给出一个代表网址 host 的字符串 base_url，和代表查询参数的列表 query_params_list，
    你需要返回带查询参数的完整 URL。
    查询参数列表由一些包含两个元素的数组组成，第一个元素代表参数，第二个元素代表该参数对应的值。
    base_url 和查询参数字符串之间使用 ? 拼接，参数和值之间通过 = 拼接，
    各个查询参数之间使用 & 拼接。查询参数需要根据字典序排序。

样例 1：
    输入：base_url = "https://www.lintcode.com/problem", query_params_list = [["typeId", "2"]]
    输出："https://www.lintcode.com/problem?typeId=2"
    解释：只有一个参数 typeId=2，直接拼接即可

样例 2：
    输入：base_url = "https://translate.google.cn/", query_params_list = [["sl", "en"], ["tl", "zh-CN"], ["text", "Hello"], ["op", "translate"]]
    输出："https://translate.google.cn/?op=translate&sl=en&text=Hello&tl=zh-CN"
    解释：参数按字典序排列，依次拼接 op、sl、text、tl
"""

from typing import (
    List,
)

class Solution:
    """
    @param base_url: the string of base_url
    @param query_params_list: sequence of two-element tuples by query_params
    @return: return a url query string
    """
    def urlencode(self, base_url: str, query_params_list: List[List[str]]) -> str:
        if len(query_params_list) == 0:
            return base_url
        # write your code.
        query_params_list.sort(key=lambda pair:pair[0])
        params = []

        for key, val in query_params_list:
            params.append(key + "=" + val)

        return base_url + "?" + "&".join(params)
