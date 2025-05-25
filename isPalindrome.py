#problem: https://leetcode.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        sa_desna = 0
        s = x
        while s > 0:
            sa_desna *= 10
            sa_desna += s%10
            s//=10

        if sa_desna == x:
            return True
        else:
            return False
