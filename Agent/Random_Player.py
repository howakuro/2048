import random
class Random_Player():
    def select_action(self,board):
        return random.choice(["r","l","u","d"])