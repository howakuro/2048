from environment.Game.Game import Game
import numpy as np
import random 
from multiprocessing import Pool
import multiprocessing as multi


class Montecarlo_Player():
    def __init__(self,sim_num = 100):
        self.sim_num = sim_num
        self.move_list = [0,1,2,3]

    def random_sim(self,List):
        count = 1
        game = Game(List[0])
        game.flick(List[1])
        key_flick = [game.flick_right,game.flick_left,game.flick_up,game.flick_down]
        while game.playable():
            if random.choice(key_flick)():
                game.put_tile()
                count += 1
        return count + game.score + np.max(game.board)

    def select_action(self,board):
        can_move_list = np.array([flick(Game(board)) for flick in (Game.flick_up, Game.flick_down,Game.flick_right,Game.flick_left)])
        move_index = np.where(can_move_list == True)[0]
        count = {0:0,1:0,2:0,3:0} 
        for i in move_index:
            move = self.move_list[i]
            List = [[board,move] for j in range(self.sim_num)]
            with Pool(4) as p:
                List = [[board,move] for j in range(self.sim_num)]
                callback =  p.map(self.random_sim,List)
            count[move] = sum(callback) / self.sim_num
        print(count)
        return max(count, key=count.get)

def simulation():
    game = Game()
    game.put_tile()
    game.put_tile()
    print(game.board)
    player = Montecarlo_Player(100)    
    key_flick = {"r":game.flick_right,"l":game.flick_left,"u":game.flick_up,"d":game.flick_down}
    while game.playable():
        if key_flick[player.select_action(game.board)]():
            game.put_tile()
            print(game.board)
            print("score:",game.score,"\n")

if __name__ == "__main__":
    simulation()

        