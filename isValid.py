#problem: https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, x):
        stack = []
        recnik = {')': '(', '}': '{', ']':'['}
        for i in x:
            if i in recnik:
                if stack and recnik[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False