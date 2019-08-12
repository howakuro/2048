from Game import Game 
from Agent.Montecarlo_Player import Montecarlo_Player
from Agent.Random_Player import Random_Player
from Agent.AlphaBeta_Player import AlphaBeta_Player
from Agent.RuleBased_Player import RuleBased_Player

def play_game(game, agent, show_board, show_score):
    key_flick = {"r":game.flick_right,"l":game.flick_left,"u":game.flick_up,"d":game.flick_down}
    game.reset()
    game.put_tile()
    game.put_tile()
    if show_board:
        print(game.board)
    while game.playable():
        action = agent.select_action(game.board)
        if key_flick[action]():
            game.put_tile()
            if show_score:
                print(f'\nscore = {game.score}')
            if show_board:
                print(game.board)

def simulater(agent = Random_Player(), simulation = 1, episode = 1, show_board = False, show_score = False):
    game = Game()
    for sim_num in range(simulation):
        for epi_num in range(episode):
            play_game(game, agent, show_board, show_score)
            
def main():
    agent_list = [RuleBased_Player()]
    for agent in agent_list:
        simulater(agent = agent, show_board=True, show_score=True)

if __name__ == "__main__":
    main()

