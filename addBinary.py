#problem: https://leetcode.com/problems/add-binary/description/
class Solution(object): # first solution
    def addBinary(self, x, y):
        ostatak = 0
        final = ''
        xx = int(x)
        yy = int(y)
        while True:
            if xx == 0 and yy == 0 and ostatak == 1:
                final = '1' + final
                break
            if xx == 0 and yy == 0 and ostatak == 0:
                final = '0' + final
                break
            t = xx % 10
            m = yy % 10
            if t == 1 and m == 1 and ostatak == 0:
                final = '0' + final
                ostatak = 1
            elif t == 1 and m == 1 and ostatak == 1:
                final = '1' + final
            elif (t == 1 and m == 0 and ostatak == 1) or (t == 0 and m == 1 and ostatak == 1):
                final = '0' + final
            elif (t == 1 and m == 0 and ostatak == 0) or (t == 0 and m == 1 and ostatak == 0):
                final = '1' + final
            elif t == 0 and m == 0 and ostatak == 1:
                final = '1' + final
                ostatak = 0
            elif t == 0 and m == 0 and ostatak == 0:
                final = '0' + final
            xx //= 10
            yy //= 10
        i = int(final)
        return str(i)

class Solution(object): #second solution
    def addBinary(self, x, y):
        return bin(int(x, 2) + int(y, 2))[2:]