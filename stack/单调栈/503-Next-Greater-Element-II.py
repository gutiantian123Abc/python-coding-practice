"""
503. Next Greater Element II
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number.
If it doesn't exist, return -1 for this number.


Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.


Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_2 = nums + nums
        stack = []
        map = {}

        for i, num in enumerate(nums_2):
            if not stack:
                if i < n:
                    stack.append(i)
            else:
                while stack and nums[stack[-1]] < num:
                    smaller_index = stack.pop()
                    map[smaller_index] = i % n

                if i < n:
                    stack.append(i)

        res = [-1] * n
        for smaller_index in map:
            larger_index = map[smaller_index]
            res[smaller_index] = nums[larger_index]

        return res