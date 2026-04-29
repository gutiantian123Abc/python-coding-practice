"""
471 · 最高频的K个单词
描述
给定一个单词列表和一个整数k，求出这个列表中出现频次最高的K个单词。

你需要按照单词的词频排序后输出，越高频的词排在越前面。如果两个单词出现的次数相同，则词典序小的排在前面。

样例 1:
输入:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 3
输出: ["code", "lint", "baby"]

样例 2:
输入:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 4
输出: ["code", "lint", "baby", "yes"]
"""

from typing import (
    List,
)
import heapq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def top_k_frequent_words(self, words: List[str], k: int) -> List[str]:
        # write your code here
        counter = {}
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1

        class Item:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            def __lt__(self, other):
                # min heap
                # Lower frequency is worse, so it should be popped out
                if self.freq != other.freq:
                    return self.freq < other.freq

                # If same frequency, alphabetically larger word should be popped out
                return self.word > other.word


        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, Item(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(key=lambda item: (-item.freq, item.word))

        res = []

        for item in heap:
            res.append(item.word)
        return res