from environment.Game.Game import Game
import numpy as np
import random 
from multiprocessing import Pool
import multiprocessing as multi


class Montecarlo_Player():
    def __init__(self,sim_num = 100):
        self.sim_num = sim_num
        self.move_list = [0,1,2,3]

    def random_sim(self, board, move):
        game = Game(board)
        game.flick(move)
        key_flick = [game.flick_right,game.flick_left,game.flick_up,game.flick_down]
        while game.playable():
            if random.choice(key_flick)():
                game.put_tile()
        return game.score

    def select_action(self,board):
        can_move_list = np.array([flick(Game(board)) for flick in (Game.flick_up, Game.flick_down,Game.flick_right,Game.flick_left)])
        move_index = np.where(can_move_list == True)[0]
        count = {0:0, 1:0, 2:0, 3:0} 
        for i in move_index:
            move = self.move_list[i]
            for _ in range(self.sim_num):
                count[move] += self.random_sim(board, move)
            count[move] /= self.sim_num
        print(count)
        return max(count, key=count.get)