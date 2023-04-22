import argparse

from sudoku.game import SudokuManager
from sudoku.players import SudokuPlayer, ManualPlayer, BruteForcePlayer

class SudokuGame():
    def __init__(self, 
                    player : SudokuPlayer, 
                    board_file : str,
                ):
        self.manager = SudokuManager(board_file)
        self.player  = player
    
    def get_next_move(self):
        self.check_if_won()

    def check_if_won(self, board : list) -> bool:
        """Return bool of whether a board is complete

        Args:
            board (list): contains valus of all cells of a game board

        Returns:
            bool: whether board is complete
        """
        if not self.manager.is_valid_board(board):
            return False
        for row in board:
            if ' ' in row:
                return False
        else:
            return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--board', type=str, 
                        help='Filepath for board text file')
    
    args = parser.parse_args()

    sudoku = SudokuManager(args.board)
    print(sudoku.get_print_board())
