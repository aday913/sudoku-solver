import argparse

from sudoku.game import SudokuManager
from sudoku.players import SudokuPlayer, ManualPlayer, BruteForcePlayer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--board', type=str, 
                        help='Filepath for board text file')
    
    args = parser.parse_args()

    sudoku = SudokuManager(args.board)
    print(sudoku.get_print_board())
    print(sudoku.is_valid_board(sudoku.board_vals))