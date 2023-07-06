class SudokuManager():
    def __init__(self, start_board : str):
        self.board_vals = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        self._parse_input_board(start_board)

    def _parse_input_board(self, file_):
        data = []
        with open(file_, 'r') as input_file:
            for i in input_file:
                data.append(i)

        for row in range(1,10):
            for col in range(1,10):
                val = data[(row*2)-1][(col*4)-2]
                self.board_vals[row-1][col-1] = str(val)
    
    def get_print_board(self) -> str:
        vals = self.board_vals
        print_board = f"""
            |---|---|---I---|---|---I---|---|---|
            | {vals[0][0]} | {vals[0][1]} | {vals[0][2]} I {vals[0][3]} | {vals[0][4]} | {vals[0][5]} I {vals[0][6]} | {vals[0][7]} | {vals[0][8]} |
            |---|---|---I---|---|---I---|---|---|
            | {vals[1][0]} | {vals[1][1]} | {vals[1][2]} I {vals[1][3]} | {vals[1][4]} | {vals[1][5]} I {vals[1][6]} | {vals[1][7]} | {vals[1][8]} |
            |---|---|---I---|---|---I---|---|---|
            | {vals[2][0]} | {vals[2][1]} | {vals[2][2]} I {vals[2][3]} | {vals[2][4]} | {vals[2][5]} I {vals[2][6]} | {vals[2][7]} | {vals[2][8]} |
            |===|===|===I===|===|===I===|===|===|
            | {vals[3][0]} | {vals[3][1]} | {vals[3][2]} I {vals[3][3]} | {vals[3][4]} | {vals[3][5]} I {vals[3][6]} | {vals[3][7]} | {vals[3][8]} |
            |---|---|---I---|---|---I---|---|---|
            | {vals[4][0]} | {vals[4][1]} | {vals[4][2]} I {vals[4][3]} | {vals[4][4]} | {vals[4][5]} I {vals[4][6]} | {vals[4][7]} | {vals[4][8]} |
            |---|---|---I---|---|---I---|---|---|
            | {vals[5][0]} | {vals[5][1]} | {vals[5][2]} I {vals[5][3]} | {vals[5][4]} | {vals[5][5]} I {vals[5][6]} | {vals[5][7]} | {vals[5][8]} |
            |===|===|===I===|===|===I===|===|===|
            | {vals[6][0]} | {vals[6][1]} | {vals[6][2]} I {vals[6][3]} | {vals[6][4]} | {vals[6][5]} I {vals[6][6]} | {vals[6][7]} | {vals[6][8]} |
            |---|---|---I---|---|---I---|---|---|
            | {vals[7][0]} | {vals[7][1]} | {vals[7][2]} I {vals[7][3]} | {vals[7][4]} | {vals[7][5]} I {vals[7][6]} | {vals[7][7]} | {vals[7][8]} |
            |---|---|---I---|---|---I---|---|---|
            | {vals[8][0]} | {vals[8][1]} | {vals[8][2]} I {vals[8][3]} | {vals[8][4]} | {vals[8][5]} I {vals[8][6]} | {vals[8][7]} | {vals[8][8]} |
            |---|---|---I---|---|---I---|---|---|
            """
        return print_board

    def get_val_board(self) -> list:
        return self.board_vals
    
    def check_if_won(self, board : list) -> bool:
        """Return bool of whether a board is complete

        Args:
            board (list): contains valus of all cells of a game board

        Returns:
            bool: whether board is complete
        """
        if not self.is_valid_board(board):
            return False
        for row in board:
            if ' ' in row:
                return False
        else:
            return True
    
    def is_valid_board(self, vals : list) -> bool:
        # Check rows:
        for row in vals:
            for i in range(1, 10):
                if row.count(str(i)) > 1:
                    return False
        
        # Check cols
        for i in range(9):
            col = []
            for row in vals:
                col.append(row[i])
            for j in range(1, 10):
                if col.count(str(j)) > 1:
                    return False
        
        # Check inner squares
        squares = {
            '1' : [vals[0][0], vals[0][1], vals[0][2], vals[1][0], vals[1][1], vals[1][2], vals[2][0], vals[2][1], vals[2][2]],
            '2' : [vals[0][3], vals[0][4], vals[0][5], vals[1][3], vals[1][4], vals[1][5], vals[2][3], vals[2][4], vals[2][5]],
            '3' : [vals[0][6], vals[0][7], vals[0][8], vals[1][6], vals[1][7], vals[1][8], vals[2][6], vals[2][7], vals[2][8]],
            '4' : [vals[3][0], vals[3][1], vals[3][2], vals[4][0], vals[4][1], vals[4][2], vals[5][0], vals[5][1], vals[5][2]],
            '5' : [vals[3][3], vals[3][4], vals[3][5], vals[4][3], vals[4][4], vals[4][5], vals[5][3], vals[5][4], vals[5][5]],
            '6' : [vals[3][6], vals[3][7], vals[3][8], vals[4][6], vals[4][7], vals[4][8], vals[5][6], vals[5][7], vals[5][8]],
            '7' : [vals[6][0], vals[6][1], vals[6][2], vals[7][0], vals[7][1], vals[7][2], vals[8][0], vals[8][1], vals[8][2]],
            '8' : [vals[6][3], vals[6][4], vals[6][5], vals[7][3], vals[7][4], vals[7][5], vals[8][3], vals[8][4], vals[8][5]],
            '9' : [vals[6][6], vals[6][7], vals[6][8], vals[7][6], vals[7][7], vals[7][8], vals[8][6], vals[8][7], vals[8][8]]
        }
        for num in squares.keys():
            for i in range(1, 10):
                if squares[num].count(str(i)) > 1:
                    return False
        
        return True