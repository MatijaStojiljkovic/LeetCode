#problem: https://leetcode.com/problems/divide-two-integers/
import math
class Solution:
    def divide(self, x: int, y: int) -> int:
        z = 0
        if (x > 0 and y > 0) or (x < 0 and y < 0):
            z = math.floor(x/y)
        elif (x < 0 and y > 0) or (x>0 and y<0):
            z = math.ceil(x/y)
        if z >= 2147483648:
            return 2147483647
        elif z < -2147483648:
            return -2147483648
        else: return z