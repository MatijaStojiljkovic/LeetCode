class Solution(object):
    def myAtoi(self, x):
        num = 0
        sign = True
        nadjen_broj = False
        nadjen_znak = False
        for i in x:
            if num == 0 and i == " " and nadjen_broj == False and nadjen_znak == False:
                continue
            elif num == 0 and i == "-" and nadjen_broj == False and nadjen_znak == False:
                sign = False
                nadjen_znak = True
            elif num == 0 and i == "+" and nadjen_broj == False and nadjen_znak == False:
                nadjen_znak = True
                continue
            elif i.isdigit():
                num *= 10
                num += int(i)
                nadjen_broj = True
            elif not i.isdigit():
                break
        if sign == False:
            num = -num
        if not -2147483648 <= num:
            num = -2147483648
        elif not num <= 2147483647:
            num = 2147483647

        return num
