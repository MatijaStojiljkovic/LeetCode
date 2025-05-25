#problem: https://leetcode.com/problems/remove-element/
class Solution(object):
    def removeElement(self, x, y):
        i = 0
        while i < len(x):
            if x[i] == y:
                x.remove(x[i])
            else: i+=1
        return len(x)