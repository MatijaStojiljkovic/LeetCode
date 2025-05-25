#problem: https://leetcode.com/problems/contains-duplicate/description/
class Solution(object):
    def containsDuplicate(self, x):
        y = set()
        for i in x:
            if i in y:
                return True
            else:
                y.add(i)


        return False