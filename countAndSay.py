#problem: https://leetcode.com/problems/count-and-say/description/
class Solution:
    def countAndSay(self, n: int) -> str:
            if n == 1:
                return '1'
            result = ""
            prev = self.countAndSay(n-1)
            count = 1
            for i in range(len(prev)):
                if i + 1 < len(prev) and prev[i] == prev[i+1]:
                    count+=1
                else:
                    result += str(count) + prev[i]
                    count = 1
            return result