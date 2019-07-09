A customised package for building simulation environment.  

### Dependences:  
gym  
```
gym: $ pip install gym  
```
EnergyPlus  
specify environment variables  

### Installation:  
git clone this repository and install  
```
$ cd gym_energyplus  
$ pip install -e .
```
### Usage:
```
import gym
import gym_energyplus
env = gym.make('gym_energyplus:EnergyPlus-v0')  

observation = env.reset()  
action =  env.action_space.sample()   
observation, reward, done, info = env.step(action)  
```
