import gym
import Agent

if __name__ == "__main__":
    for i in range(1):
        env = gym.make('Gym_2048-v0')
        agent = Agent.Random_Player()
        obs = env.reset()
        done = False
        env.render()
        while not done:
            action = agent.select_action(obs)
            obs, reward, done, info = env.step(action)
            env.render()
            