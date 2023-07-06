import argparse
import sys

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
        won_bool = self.manger.check_if_won()
        if won_bool:
            print('Congratulation! You have won the game!')
            sys.exit()
        else:
            
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--board', type=str, 
                        help='Filepath for board text file')
    
    args = parser.parse_args()

    game = SudokuGame(SudokuPlayer,args.board)
    print(game.manager.get_print_board())
