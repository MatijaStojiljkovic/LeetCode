#problem: https://leetcode.com/problems/fruits-into-baskets-ii/description/
class Solution:
    def numOfUnplacedFruits(self, voca: List[int], korpe: List[int]) -> int:
        count = 0
        boolovi = [False for _ in range(len(korpe))]
        for i in range(len(voca)):
            for j in range(len(korpe)):
                if voca[i] <= korpe[j] and boolovi[j] == False:
                    boolovi[j] = True
                    break
                elif (voca[i] > korpe[j] or boolovi[j] == True) and j + 1 == len(korpe):
                    count += 1
        return count