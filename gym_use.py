import gym
import gym_datacenter
env = gym.make('gym_datacenter:datacenter-v0')  

observation = env.reset()  
print(observation)
action =  env.action_space.sample()   
print(action)
observation, reward, done, info = env.step(action) 
print(observation)
env.close()