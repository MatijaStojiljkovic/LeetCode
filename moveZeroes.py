#problem: https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, x):
        i = 0
        brojac = 0
        while i < len(x):
            if x[i] == 0:
                x.remove(x[i])
                brojac+=1
            else: i+=1
        for i in range(brojac):
            x.append(0)
        return x