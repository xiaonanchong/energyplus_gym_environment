import matplotlib.pyplot as plt
%matplotlib inline

import gym
import gym_energyplus
env = gym.make('gym_energyplus:EnergyPlus-v0') 

episode_length = 96 # 1day

observation = env.reset()
for i in range(episode_length):
	action = env.action_space.sample()
	observation, reward, done, info = env.step(action)

	      
    	plt.plot(i+1, observation[0], 'go')
    	plt.plot(i+1, observation[1], 'co')
    	plt.plot(i+1, observation[2], 'm+')
    	plt.plot(i+1, observation[4]/r, 'r_')
    	plt.plot(i+1, observation[5]/r, 'y_')
    	plt.plot(i+1, observation[3]/r, 'k_')
plt.legend()
plt.show()
