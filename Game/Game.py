import random
import os
from numba import jit 
import numpy as np
import copy as cp
SIZE = 4
DIGITS = 4

class Game:
    def __init__(self, board=None):
        self.reset(board)

    def reset(self,board=None):
        self.board = np.zeros((SIZE,SIZE),dtype = int) if np.all(board == None) else np.copy(board)
        self.score = 0.0
    
    def move_left(self):
        moved = False
        for row in self.board:
            for left in range(SIZE - 1):
                for right in range(left + 1, SIZE):
                    if row[right] == 0:
                        continue
                    if row[left] == 0:
                        row[left] = row[right]
                        row[right] = 0
                        moved = True
                        continue
                    if row[left] == row[right]:
                        self.score += row[right] * 2
                        row[left] += row[right]
                        row[right] = 0
                        moved = True
                        break
                    if row[left] != row[right]:
                        break
        return moved
    
    def rotate_left(self):
        self.board = np.rot90(self.board, k=1)

    
    def rotate_right(self):
        self.board = np.rot90(self.board, k=-1)

    
    def rotate_turn(self):
        self.rotate_left()
        self.rotate_left()
    
    
    def flick(self,key):
        if key == "u":
            self.flick_up()
        elif key == "d":
            self.flick_down()
        elif key == "r":
            self.flick_right()
        elif key == "l":
            self.flick_left()
   
    def flick_left(self):
        moved = self.move_left()
        return moved
    
    def flick_right(self):
        self.rotate_turn()
        moved = self.move_left()
        self.rotate_turn()
        return moved

    
    def flick_up(self):
        self.rotate_left()
        moved = self.move_left()
        self.rotate_right()
        return moved

    def flick_down(self):
        self.rotate_right()
        moved = self.move_left()
        self.rotate_left()
        return moved
    
    def playable(self):
        return any(flick(Game(self.board)) 
                   for flick in (Game.flick_left, Game.flick_right,Game.flick_up, Game.flick_down))
    
    def can_put_list(self):
        y,x = np.where(self.board == 0)
        return y,x

    def put_tile(self, pos = None):
        if pos == None: 
            y,x = self.can_put_list()
            num = np.random.choice(np.arange(len(y)))
            self.board[y[num]][x[num]] = np.random.choice((2, 4), p=[0.8, 0.2])
        else:
            y, x = pos
            self.board[y][x] = np.random.choice((2, 4), p=[0.8, 0.2])

def random_simulation(board = None):
        game = Game(board)
        if np.all(board == None):
            game.put_tile()
            game.put_tile()
            print(game.board)
        key_flick = [game.flick_right,game.flick_left,game.flick_up,game.flick_down]
        while game.playable():
            if random.choice(key_flick)():
                game.put_tile()
                print(game.board)
                print(f'score = {game.score}')

if __name__ == '__main__':
    random_simulation()