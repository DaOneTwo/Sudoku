from Objects.board import SudokuBoard


class SudokuSolver(SudokuBoard):
    def __init__(self, data_set):
        super(SudokuSolver, self).__init__(data_set)

        self._row_col_mapper = {num: letter for num, letter in zip(self._row_nums, self._col_letters)}

        self.build_columns_and_blocks()

    def print_data_set(self, data_set):
        [print(d_list) for d_list in data_set]

    def solve(self):
        """Solves the puzzle, what else would it do?"""


if __name__ == '__main__':

    data = '1,2,5,3,7,8,9,4,6,3,7,8,9,5,4,2,1,5,4,9,6,1,2,5,8,3,7,2,6,9,4,5,3,1,7,8,8,4,1,7,9,2,6,5,3,5,3,7,8,1,6,4,9,2,9,1,2,5,8,7,3,6,4,6,5,3,2,4,9,7,,1,7,8,4,6,3,1,5,2,9'

    exec_obj = SudokuSolver(data)
    # exec_obj = SudokuValidator(puzzle)
    # exec_obj.print_board()
    exec_obj.print_data_set(exec_obj.columns)