# Import Library
import gym

#Create simulation instance
env = gym.make('CartPole-v0')

#Initialize environment
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())