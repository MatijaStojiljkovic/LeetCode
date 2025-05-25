#problem: https://leetcode.com/problems/valid-sudoku/description/
class Solution(object):
    def isValidSudoku(self, x):
        stack = [[False for _ in range(9)] for _ in range(9)]
        stack2 = [[False for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if x[i][j].isdigit():
                    num = int(x[i][j]) - 1
                    if not stack[i][num]:
                        stack[i][num] = True
                    elif stack[i][num]:
                        return False
        for i in range(9):
            for j in range(9):
                if x[j][i].isdigit():
                    num = int(x[j][i]) - 1
                    if not stack2[num][i]:
                        stack2[num][i] = True
                    elif stack2[num][i]:
                        return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = [False] * 9
                for i in range(3):
                    for j in range(3):
                        cell_value = x[box_row + i][box_col + j]
                        if cell_value != '.':
                            num = int(cell_value) - 1
                            if seen[num]:
                                return False
                            seen[num] = True
        return True
