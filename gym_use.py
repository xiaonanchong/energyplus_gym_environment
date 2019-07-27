import gym
import gym_datacenter
env = gym.make('gym_datacenter:datacenter-v0')  

for i in range(4):
  observation = env.reset()  
  print('St:')
  print(observation)
  action =  env.action_space.sample()  
  print('At')
  print(action)
  observation, reward, done, info = env.step(action) 
  print('St+1')
  print(observation)
  
env.close()
