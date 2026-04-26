"""
872 · 终止进程
描述
这个问题中. 每个进程都有一个唯一的 PID(进程id) 和 PPID(父进程id)。
每个进程只有一个父进程，但可能有一个或多个子进程，
这就像一个树形结构。并且只有一个进程的PPID是0，这意味着这个进程没有父进程。所有的pid都是不同的正整数。

我们使用两个整数列表来表示进程列表，其中第一个列表包含每个进程的PID，第二个列表包含对应的PPID。

现在给定这两个列表，以及一个你要终止(kill)的进程的ID，返回将在最后被终止的进程的PID列表。
(当一个进程被终止时，它的所有子进程将被终止。返回的列表没有顺序要求）

1.给定的kill id一定是PID列表中的某个id
2.给定的PID列表中至少含有一个进程

样例 1:
输入: PID = [1, 3, 10, 5], PPID = [3, 0, 5, 3], killID = 5
输出: [5, 10]
解释: 终止进程5同样会终止进程10.
     3
   /   \
  1     5
       /
      10

样例 2:
输入: PID = [1, 2, 3], PPID = [0, 1, 1], killID = 2
输出: [2]
"""

from typing import (
    List,
)
from collections import deque

class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
             we will sort your return value in output
    """
    def kill_process(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # Write your code here
        children_map = {}
        for i in range(len(ppid)):
            parent = ppid[i]
            child = pid[i]

            if parent not in children_map:
                children_map[parent] = []

            children_map[parent].append(child)

        result = []
        queue = deque()
        queue.append(kill)

        while queue:
            size = len(queue)
            for i in range(size):
                p = queue.popleft()
                result.append(p)
                if p in children_map:
                    for child in children_map[p]:
                        queue.append(child)

        return result