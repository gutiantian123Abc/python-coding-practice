"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.


Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.


Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        nums[n]
        dp[n+1]
        sum[i ~ j] = dp[j + 1] - dp[i]
        """
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + nums[i - 1]

        prev_min_sum = dp[0]
        res = nums[0]
        for i in range(1, n + 1):
            res = max(res, dp[i] - prev_min_sum)
            prev_min_sum = min(dp[i], prev_min_sum)

        return res