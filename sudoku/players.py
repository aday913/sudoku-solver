class SudokuPlayer():
    def __init__(self):
        self.knowledge_base = {
            '0,0' : [], '0,1' : [], '0,2' : [], '0,3' : [], '0,4' : [], '0,5' : [], '0,6' : [], '0,7' : [], '0,8' : [],
            '1,0' : [], '1,1' : [], '1,2' : [], '1,3' : [], '1,4' : [], '1,5' : [], '1,6' : [], '1,7' : [], '1,8' : [],
            '2,0' : [], '2,1' : [], '2,2' : [], '2,3' : [], '2,4' : [], '2,5' : [], '2,6' : [], '2,7' : [], '2,8' : [],
            '3,0' : [], '3,1' : [], '3,2' : [], '3,3' : [], '3,4' : [], '3,5' : [], '3,6' : [], '3,7' : [], '3,8' : [],
            '4,0' : [], '4,1' : [], '4,2' : [], '4,3' : [], '4,4' : [], '4,5' : [], '4,6' : [], '4,7' : [], '4,8' : [],
            '5,0' : [], '5,1' : [], '5,2' : [], '5,3' : [], '5,4' : [], '5,5' : [], '5,6' : [], '5,7' : [], '5,8' : [],
            '6,0' : [], '6,1' : [], '6,2' : [], '6,3' : [], '6,4' : [], '6,5' : [], '6,6' : [], '6,7' : [], '6,8' : [],
            '7,0' : [], '7,1' : [], '7,2' : [], '7,3' : [], '7,4' : [], '7,5' : [], '7,6' : [], '7,7' : [], '7,8' : [],
            '8,0' : [], '8,1' : [], '8,2' : [], '8,3' : [], '8,4' : [], '8,5' : [], '8,6' : [], '8,7' : [], '8,8' : [],
        }
    
    def add_to_kb(self, loc, value):
        if int(value) >= 0 and int(value) <= 9:
            if value not in self.knowledge_base[loc]:
                self.knowledge_base[loc].append(value)
            else:
                print(f'{value} is already in knowledge base for location {loc}')
        else:
            print(f'{value} is not a valid sudoku square value, try again')
    
    def get_kb(self) -> dict:
        return self.knowledge_base

    def get_kb_for_loc(self, loc):
        try:
            return self.knowledge_base[loc]
        except Exception as error:
            print(f'Cannot perform operation: {error}')

class ManualPlayer(SudokuPlayer):
    def __init__(self):
        super().__init__()
    
    
class LogicPlayer(SudokuPlayer):
    def __init__(self):
        super().__init__()
        
class SearchPlayer(SudokuPlayer):
    def __init__(self):
        super().__init__()