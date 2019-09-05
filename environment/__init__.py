from .Game import Game
from .gym_2048 import Gym_2048
from gym.envs.registration import register
register(
  id='Gym_2048-v0',
  entry_point='environment.gym_2048:Gym_2048'
)