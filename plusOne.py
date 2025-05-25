#problem: https://leetcode.com/problems/plus-one/description/
class Solution(object):
    def plusOne(self, x):
        broj = 0
        for i in range(len(x)):
            broj *= 10
            broj += x[i]
        broj+=1
        m = broj
        broj_cifara = 0
        while m > 0:
            m//=10
            broj_cifara+=1


        if broj_cifara > len(x):
            x.append(0)
        for i in range(1, len(x)+1):
            x[-i] = broj % 10
            broj //= 10
        return x