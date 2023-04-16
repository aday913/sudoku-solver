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
        pass

    def check_if_won(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--board', type=str, 
                        help='Filepath for board text file')
    
    args = parser.parse_args()

    sudoku = SudokuManager(args.board)
    print(sudoku.get_print_board())
