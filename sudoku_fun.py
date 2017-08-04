import sys

from Objects.validator import SudokuValidator
from Objects.solver import SudokuSolver


puzzle_list = [
    #invalid
# '1,2,3,4,5,6,7,8,9,' * 8 + '1,2,3,4,5,6,7,8,9',
# '1,2,5,3,7,8,9,4,6,3,7,8,9,5,4,2,1,5,4,9,6,1,2,5,8,3,7,2,6,9,4,5,3,1,7,8,8,4,1,7,9,2,6,5,3,5,3,7,8,1,6,4,9,2,9,1,2,5,8,7,3,6,4,6,5,3,2,4,9,7,8,1,7,8,4,6,3,1,5,2,9',
'1,2,5,3,7,8,9,4,6,3,7,8,9,5,4,2,1,5,4,9,6,1,2,5,8,3,7,2,6,9,4,5,3,1,7,8,8,4,1,7,9,2,6,5,3,5,3,7,8,1,6,4,9,2,9,1,2,5,8,7,3,6,4,6,5,3,2,4,9,7,,1,7,8,4,6,3,1,5,2,9',
    # Valid
# '1,2,5,3,7,8,9,4,6,3,7,8,9,6,4,2,1,5,4,9,6,1,2,5,8,3,7,2,6,9,4,5,3,1,7,8,8,4,1,7,9,2,6,5,3,5,3,7,8,1,6,4,9,2,9,1,2,5,8,7,3,6,4,6,5,3,2,4,9,7,8,1,7,8,4,6,3,1,5,2,9',
]

for line in sys.stdin.readline():
    print(line)

# validate Solution
for puzzle in puzzle_list:
    exec_obj = SudokuSolver(puzzle)
    # exec_obj = SudokuValidator(puzzle)
    # exec_obj.print_board()
    exec_obj.print_data_set(exec_obj.columns)
    print('')