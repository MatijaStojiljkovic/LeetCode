#problem: https://leetcode.com/problems/valid-number/description/
class Solution:
    def isNumber(self, x: str) -> bool:
        nadjen_znak = False
        krenuo_broj = False
        nadjen_eksponent = False
        nadjen_decimal = False
        for i in range(len(x)):
            if x[i] == "+" and not nadjen_znak and not krenuo_broj and i + 1 < len(x):
                nadjen_znak = True
                continue
            elif x[i] == "+" and (nadjen_znak or krenuo_broj or i+1 == len(x)):
                return False
            elif x[i] == "-" and not nadjen_znak and not krenuo_broj and i + 1 < len(x):
                nadjen_znak = True
                continue
            elif x[i] == "-" and (nadjen_znak or krenuo_broj or i + 1< len(x)):
                return False
            elif not x[i].isdigit() and x[i] != "e" and x[i] != "E" and x[i] != ".":
                return False
            elif (i + 1 < len(x) and x[i] == "." and not x[i + 1].isdigit() and x[i + 1] != 'E' and x[i + 1] != "e") or (x[i] == "." and i + 1 == len(x) and not krenuo_broj) or (x[i] == "." and nadjen_decimal):
                return False
            elif x[i] == '.' and nadjen_eksponent:
                return False
            elif (i + 1 < len(x) and (x[i] == "e" or x[i] == "E") and ((not x[i + 1].isdigit() and x[i+1] != "+" and  x[i+1] != "-") or (not krenuo_broj or nadjen_eksponent))) or (x[i] == "e" or x[i] == "E") and i + 1 == len(x):
                return False
            elif x[i].isdigit() or x[i] == "e" or x[i] == "E":
                krenuo_broj = True
            if x[i] == "e" or x[i] == "E":
                nadjen_eksponent = True
                nadjen_znak = False
                krenuo_broj = False
            if x[i] == ".":
                nadjen_decimal = True
        return True