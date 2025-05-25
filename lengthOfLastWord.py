#problem: https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        return len(x[-1])