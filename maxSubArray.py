#problem: https://leetcode.com/problems/maximum-subarray/description/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        ans = 0
        ans = max(nums)
        for i in range(len(nums)):
            sum += nums[i]
            if sum > ans: ans = sum
            if sum < 0:
                sum = 0


        return ans