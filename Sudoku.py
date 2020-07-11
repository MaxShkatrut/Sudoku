import time
import numpy as np

# Example:
# sudoku_giv[0][:] = [9, 0, 6, 0, 7, 0, 4, 0, 3]
# sudoku_giv[1][:] = [0, 0, 0, 4, 0, 0, 2, 0, 0]
# sudoku_giv[2][:] = [0, 7, 0, 0, 2, 3, 0, 1, 0]
# sudoku_giv[3][:] = [5, 0, 0, 0, 0, 0, 1, 0, 0]
# sudoku_giv[4][:] = [0, 4, 0, 2, 0, 8, 0, 6, 0]
# sudoku_giv[5][:] = [0, 0, 3, 0, 0, 0, 0, 0, 5]
# sudoku_giv[6][:] = [0, 3, 0, 7, 0, 0, 0, 5, 0]
# sudoku_giv[7][:] = [0, 0, 7, 0, 0, 5, 0, 0, 0]
# sudoku_giv[8][:] = [4, 0, 5, 0, 1, 0, 7, 0, 8]

# Solutions:
# 9 2 6 5 7 1 4 8 3
# 3 5 1 4 8 6 2 7 9
# 8 7 4 9 2 3 5 1 6
# 5 8 2 3 6 7 1 9 4
# 1 4 9 2 5 8 3 6 7
# 7 6 3 1 A B 8 2 5
# 2 3 8 7 C D 6 5 1
# 6 1 7 8 3 5 9 4 2
# 4 9 5 6 1 2 7 3 8

# A B => 9 4   or   4 9
# C D => 4 9   or   9 4

# Given Sudoku
sudoku_giv = np.zeros([9, 9])
sudoku_giv[0][:] = [2, 1, 0, 0, 0, 0, 4, 0, 0]
sudoku_giv[1][:] = [0, 0, 0, 0, 2, 8, 0, 0, 0]
sudoku_giv[2][:] = [0, 0, 0, 0, 0, 0, 1, 0, 6]
sudoku_giv[3][:] = [0, 0, 0, 5, 0, 7, 6, 0, 8]
sudoku_giv[4][:] = [8, 3, 0, 0, 0, 0, 0, 0, 7]
sudoku_giv[5][:] = [0, 0, 0, 0, 1, 6, 0, 0, 3]
sudoku_giv[6][:] = [0, 4, 2, 3, 0, 0, 0, 0, 0]
sudoku_giv[7][:] = [0, 5, 3, 0, 0, 0, 0, 7, 0]
sudoku_giv[8][:] = [0, 0, 7, 9, 0, 0, 0, 0, 0]

sudoku_giv = sudoku_giv.astype(int)

# Check if the position of number {num} is legal
def is_legal(num, i, j):
        if (num not in sudoku_sol[i]) and (num not in np.array(sudoku_sol).transpose()[j]):
                if (i>=0 and i<=2) and (j>=0 and j<=2):
                        if (num not in np.array(sudoku_sol[0:3]).transpose()[0:3]):
                                return True
                elif (i>=0 and i<=2) and (j>=3 and j<=5):
                        if (num not in np.array(sudoku_sol[0:3]).transpose()[3:6]):
                                return True
                elif (i>=0 and i<=2) and (j>=6 and j<=8):
                        if (num not in np.array(sudoku_sol[0:3]).transpose()[6:9]):
                                return True
                elif (i>=3 and i<=5) and (j>=0 and j<=2):
                        if (num not in np.array(sudoku_sol[3:6]).transpose()[0:3]):
                                return True
                elif (i>=3 and i<=5) and (j>=3 and j<=5):
                        if (num not in np.array(sudoku_sol[3:6]).transpose()[3:6]):
                                return True
                elif (i>=3 and i<=5) and (j>=6 and j<=8):
                        if (num not in np.array(sudoku_sol[3:6]).transpose()[6:9]):
                                return True
                elif (i>=6 and i<=8) and (j>=0 and j<=2):
                        if (num not in np.array(sudoku_sol[6:9]).transpose()[0:3]):
                                return True
                elif (i>=6 and i<=8) and (j>=3 and j<=5):
                        if (num not in np.array(sudoku_sol[6:9]).transpose()[3:6]):
                                return True
                elif (i>=6 and i<=8) and (j>=6 and j<=8):
                        if (num not in np.array(sudoku_sol[6:9]).transpose()[6:9]):
                                return True
        return False

# The backtracking recursive function that checks the combinations
def check_sudoku_solution(sudoku_giv, sudoku_sol, pos, solutions):
        if pos == 81:
                solutions.append(np.array(sudoku_sol))
                return True

        res = False

        i = int(pos/9)
        j = pos % 9
        if sudoku_giv[i][j] == 0:
                for num in range(9):
                        if is_legal(num+1, i, j):
                                sudoku_sol[i][j] = num + 1

                                res = check_sudoku_solution(sudoku_giv, sudoku_sol, pos+1, solutions) or res

                                sudoku_sol[i][j] = 0
        else:
                check_sudoku_solution(sudoku_giv, sudoku_sol, pos+1, solutions)

        return res

# Main code
start_time = time.time()
sudoku_sol = list(np.zeros([9, 9]))
sudoku_sol = sudoku_giv
solutions = []
check_sudoku_solution(sudoku_giv, sudoku_sol, 0, solutions)

num_of_sols = len(solutions)
print('Running time: %.5f seconds' % (time.time() - start_time))
print('Total number of corrected solutions: %d' % num_of_sols)
for i in range(num_of_sols):
        print("Solution number %d:" % (i+1))
        print(solutions[i])

