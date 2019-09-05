import math
import copy
import numpy as np
from environment.Game.Game import Game
class AlphaBeta_Player():
    def __init__(self,depth = 3):
        self.depth = depth
        self.move_list = [0,1,2,3]

    def evaluate(self,game):
        emptyCells = len(np.where(game.board == 0)[0])
        max_value = np.log2(np.max(game.board)) 
        score = game.score
        smoothness = 0
        for y in range(4):
            for x in range(4):
                for vy,vx in [(-1,0),(0,1)]:
                    try:
                        smoothness -= abs(game.board[y+vy][x+vx])
                    except:
                        pass
        return smoothness * 0.1 + np.log(emptyCells) * 2.7 + max_value
        
    def search(self, game, depth, alpha, beta, turn):
        if not game.playable():
            return -float("inf")
        if depth == 0:
            return game.score #self.evaluate(game) 
        if turn == "move":
            for flick in [0,1,2,3]:
                copy_game = copy.deepcopy(game)
                copy_game.flick(flick)
                alpha = max((alpha, self.search(copy_game, depth-1, alpha, beta, "put") ) )
                if alpha >= beta:
                    break
            return alpha
        else:
            y,x = game.can_put_list()
            for i in range(len(y)): 
                copy_game = copy.deepcopy(game)
                copy_game.put_tile((y[i],x[i]))
                beta = min( (beta, self.search(copy_game, depth-1, alpha, beta, "move") ) )
                if alpha >= beta:
                    break
            return beta
                
    def select_action(self,board):
        can_move_list = np.array([flick(Game(board)) for flick in (Game.flick_right,Game.flick_left,Game.flick_up, Game.flick_down)])
        move_index = np.where(can_move_list == True)[0]
        move_score = {0:-float('inf'),1:-float('inf'),2:-float('inf'),3:-float('inf')}
        for index in move_index:
            flick = self.move_list[index]
            copy_game = copy.deepcopy(Game(board))
            copy_game.flick(flick)
            move_score[flick] = self.search(copy_game, self.depth, -float('inf'), float('inf'), "put")
        print(move_score)
        return max(move_score, key=move_score.get)