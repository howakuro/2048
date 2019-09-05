from . import Game
import gym
import numpy as np

class Gym_2048(gym.Env):
    def __init__(self):
        super().__init__()
        self.env = Game.Game()
        self.action_space = gym.spaces.Discrete(4) #上:0 下:1 左:2 右:3
        self.observation_space = self.env.board.shape
        self._action = None

    def reset(self):
        self.env.reset()
        return np.copy(self.env.board) 
    
    def step(self, action):
        self._action = action
        info = {"moved":False}
        moved = self.env.flick(action)
        if moved:
            self.env.put_tile()
            info["moved"] = True
        done = not self.env.playable()
        reward = self._get_reward(done, moved)
        next_state = np.copy(self.env.board)
        info["score"] = self.env.score
        return next_state, reward, done, info
    
    def render(self, mode="terminal"):
        if mode == "terminal":
            action_dict = {0:"up", 1:"down", 2:"right", 3:"left",None:"none"}
            print(f"\naction = {action_dict[self._action]}")
            print(f'score = {self.env.score}')
            print(self.env.board)

    def close(self):
        pass

    def seed(self, seed=None):
        pass    
    
    def _get_reward(self, done, moved):
        if done:
            reward = 1
        elif not moved:
            reward = -1
        else:
            reward = -1
        return reward
    
    

            
        
        



