import numpy as np
class RuleBased_Player():
    def __init__(self):
        self.previous_board = np.zeros((4,4))
        self.no_change_count = 0
        self.Key_List = [1, 2]
        self.i = 0
    def select_action(self,board):
        move = self.Key_List[self.i % 2]
        if np.allclose(self.previous_board, board):
            self.no_change_count += 1
            if self.no_change_count == 2:
                move = "l"
            if self.no_change_count == 3:
                move = "u"
        else:
            self.no_change_count = 0
        self.i += 1
        self.previous_board = np.copy(board)
        return move