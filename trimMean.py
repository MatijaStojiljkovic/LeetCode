#problem: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/description/
class Solution:
    def trimMean(self, lista: List[int]) -> float:
        l = lista.sort()
        x = len(lista)
        x = int(0.05*x)
        zbir = 0


        for i in range(x, len(lista)- x, 1):
            zbir += lista[i]
        k = float("{:.5f}".format(zbir / (len(lista)- 2*x)))
        return k