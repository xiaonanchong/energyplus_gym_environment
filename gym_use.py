import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

import gym
import gym_datacenter
env = gym.make('gym_datacenter:datacenter-v0')  

power = []
T1 = []
T2 = []
for i in range(4*12):
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
  power.append(observation[3])
  
  z1 = observation[1]
  z2 = observation[2]
  T1.append(z1)
  T2.append(z2)
  r = 1/np.absolute(22-z1) + 1/np.absolute(22-z2)
  print('reward should be', r)

plt.plot(power)
plt.plot(T1)
plt.plot(T2)
plt.savefig('gym_use.png')
#env.close()
