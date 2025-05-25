#problem: https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, x):
        least = 9223372036854775807
        isti = True
        broj = -1
        for i in range(len(x)):
            if len(x[i]) < least:
                least = len(x[i])
        for i in range(least):
            for j in range(len(x)):
                if j + 1 < len(x):
                    if x[j][i] != x[j + 1][i]:
                        isti = False
            if isti != True:
                break
            else:
                broj += 1
        if broj == -1:
            return ""
        else:
            text = ""
            for i in range(broj + 1):
                text += x[0][i]
            return text
