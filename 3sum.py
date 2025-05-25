#problem: https://leetcode.com/problems/3sum/
class Solution(object):
    def threeSum(self, x):
        res = []
        x.sort()
        for i in range(len(x)):
            if i > 0 and x[i] == x[i-1]:
                continue
            l, r = i+1, len(x) - 1
            while l < r:
                sum = x[i] + x[l] + x[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([x[i], x[l], x[r]])
                    l+=1
                    while x[l] == x[l-1] and l<r:
                        l+=1
        return res
