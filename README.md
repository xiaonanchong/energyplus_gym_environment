A customised package for building simulation environment.  

Dependences:  
```
gym: $ pip install gym  
```

Installation:  
git clone this repository and install  
```
$ cd gym_energyplus  
$ pip install -e .
```
Usage:
```
import gym
env = gym.make('gym_energyplus:EnergyPlus-v0')  

observation = env.reset()  
action =  env.action_space.sample()   
observation, reward, done, info = env.step(action)  
```
