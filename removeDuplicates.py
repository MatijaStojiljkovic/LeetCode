#problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, nums) -> int:
        numswithoutduplicates = []
        for i in range(len(nums)):
            if nums[i] in numswithoutduplicates:
                continue
            else:
                numswithoutduplicates.append(nums[i])
        numswithoutduplicates.append(-1000)
        i = 0
        while i < len(nums):
            if numswithoutduplicates[i] != nums[i]:
                nums.remove(nums[i])
            else: i+=1
        return len(nums)