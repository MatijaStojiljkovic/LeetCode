#problem: https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        result = [0 for _ in range(2)]
        x = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        result[0] = i
                        result[1] = j
                        x = True
                        break
            if x:
                break
        return result