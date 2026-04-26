"""
1613 · 最高频率的IP

描述：
    给定一个字符串数组 lines，每一个元素代表一个 IP 地址，
    找到出现频率最高的 IP。

样例 1：
    输入：lines = ["192.168.1.1", "192.118.2.1", "192.168.1.1"]
    输出："192.168.1.1"
    解释："192.168.1.1" 出现 2 次，频率最高

样例 2：
    输入：lines = ["192.168.1.1", "192.118.2.1", "192.168.1.1", "192.118.2.1", "192.118.2.1"]
    输出："192.118.2.1"
    解释："192.118.2.1" 出现 3 次，频率最高
"""

from typing import (
    List,
)

class Solution:
    """
    @param ip_lines: ip  address
    @return: return highestFrequency ip address
    """
    def highest_frequency(self, ip_lines: List[str]) -> str:
        # Write your code here
        counter = {}

        for ip in ip_lines:
            if ip not in counter:
                counter[ip] = 1
            else:
                counter[ip] += 1

        max_ip = ""
        max_count = 0

        for ip in counter:
            if counter[ip] > max_count:
                max_count = counter[ip]
                max_ip = ip

        return max_ip