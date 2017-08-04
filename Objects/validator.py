from Objects.board import SudokuBoard


class SudokuValidator(SudokuBoard):

    def __init__(self, data_set=None):

        super(SudokuValidator, self).__init__(data_set)

    def is_valid_data_set(self, data_set):
        valid = True
        invalid_list = []
        for index, item in enumerate(data_set):
            if not set(item) == self._valid_set:
                valid = False
                invalid_list.append((index, item))

        return valid, invalid_list

    def validate_board(self):
        """validate the data that is currently in the board for potential conflicts"""
        if not self.rows:
            raise ValueError('No Board Data found to validate.')
        # build out the columns and blocks from the rows we have
        columns, blocks = self.build_columns_and_blocks()

        valid_columns, invalid_columns = self.is_valid_data_set(columns)
        valid_rows, invalid_rows = self.is_valid_data_set(self.rows)
        valid_blocks, invalid_blocks = self.is_valid_data_set(blocks)

        return all([valid_columns, valid_rows, valid_blocks])