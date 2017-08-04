

class SudokuBoard(object):
    """A Sudoku Board object"""
    _col_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    _row_nums = range(1, 10)
    _valid_set = {i for i in range(1, 10)}

    def __init__(self, data_set=None):
        self.rows = None
        self.columns = None
        self.blocks = None
        self.board_data = data_set

        self.load_board()

    def load_board(self):
        """We only really care about loading the horizontals of the board the rest can be built from there.
        Why horizontals?  Because that is how we read, Left to right top to bottom"""

        def load_row(csv_data, chunk_size):
            """loads a list of strings which need to be "castable" to ints or they will be turned to a None """
            for num in range(0, len(csv_data), chunk_size):
                row_data = csv_data[num:num + chunk_size]
                yield [int(i) if i else 0 for i in row_data]  # empty values will be 0

        if self.board_data:
            data = self.board_data.split(',')
            if len(data) != 81:
                raise ValueError('Length of CSV data must be 81.')
            self.rows = [chunk for chunk in load_row(data, 9)]

    def build_columns_and_blocks(self):
        """Build out columns and blocks according to the values of the rows as they currently exist"""
        # clear out any previously built columns and blocks
        self.columns = [[0 for i in range(1, 10)] for num in range(1, 10)]  # prepopulate with 0's
        self.blocks = [[] for num in range(1,10)]  # These we can just .extend because left to right top to bottom
        # fill in columns & blocks with values from current rows
        for row_index, h_list in self.index_value_generator(self.rows):
            for col_index, value in self.index_value_generator(h_list):
                if value:  # fill in column value
                    self.columns[col_index][row_index] = value
                # insert our block data (3x3 blocks)
                if col_index in {0, 3, 6}:
                    data = h_list[col_index:col_index + 3]
                    block = self.get_block_index(row_index, col_index)
                    self.blocks[block].extend(data)

        return self.columns, self.blocks

    def index_value_generator(self, a_list):
        """"""
        for index, value in enumerate(a_list):
            yield index, value

    def get_col_incrementer(self, col_index):
        incrementer = 0  # 1st 3 columns
        if col_index == 3:
            incrementer = 1
        if col_index == 6:
            incrementer = 2

        return incrementer

    def get_block_index(self, row_index, col_index):
        block = 0
        col_incrementer = self.get_col_incrementer(col_index)
        if 0 <= row_index <= 2:
            block = 0
        elif 3 <= row_index <= 5:
            block = 3
        elif 6 <= row_index <= 8:
            block = 6
        else:
            raise Exception('Invalid Row Index')

        return block + col_incrementer

    def reset_board(self):
        """reset the board to the state it was originally created in."""
        self.rows = None
        self.columns = None
        self.blocks = None

        self.load_board()

    def board_as_csv(self):
        """return the current board as a csv"""
        export_list = []
        for r_list in self.rows:
            for item in r_list:
                if item:
                    export_list.append(str(item))
                else:
                    export_list.append('')

        return ','.join(export_list)

    def print_board(self):
        if self.rows:
            for row in self.rows:
                print(row)
        else:
            print('No data found for Board')