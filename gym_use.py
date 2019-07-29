import numpy as np
import gym
import gym_datacenter
env = gym.make('gym_datacenter:datacenter-v0')  

for i in range(2):
  observation = env.reset()  
  print('St:')
  print(observation)
  action =  np.array([-0.5, -0.5, 1, 1])  
  print('At:')
  print(action)
  observation, reward, done, info = env.step(action) 
  print('St+1:')
  print(observation)
  print('reward_t:')
  print(reward)
  
  z1 = observation[1]
  z2 = observation[2]
  r = 1/np.absolute(22-z1) + 1/np.absolute(22-z2)
  print('reward should be', r)
  
#env.close()
