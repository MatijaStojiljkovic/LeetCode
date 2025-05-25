#problem: https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        broj = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i < len(s)-1:
                    if s[i+1] == "V":
                        broj += 4
                        i+=2
                    elif s[i+1] == "X":
                        broj += 9
                        i+=2
                    else:
                        broj+=1
                        i+=1
                else:
                    broj+=1
                    i+=1

            elif s[i] == "V":
                broj+=5
                i+=1
            elif s[i] == "X":
                if i < len(s)-1:
                    if s[i+1] == "L":
                        broj += 40
                        i+=2
                    elif s[i+1] == "C":
                        broj += 90
                        i+=2
                    else:
                        i+=1
                        broj+=10
                else:
                    i+=1
                    broj+=10
            elif s[i] == "L":
                broj+=50
                i+=1
            elif s[i] == "C":
                if i < len(s)-1:
                    if s[i+1] == "D":
                        broj += 400
                        i+=2
                    elif s[i+1] == "M":
                        broj += 900
                        i+=2
                    else:
                        i+=1
                        broj+=100
                else:
                    broj+=100
                    i+=1
            elif s[i] == "D":
                i+=1
                broj+=500
            elif s[i] == "M":
                i+=1
                broj+=1000
        return broj