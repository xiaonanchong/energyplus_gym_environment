A customised package for building simulation environment. following openai gym interface: https://github.com/openai/gym/blob/master/docs/creating-environments.md   

### Dependences:  
python version > 3.5  
gym  
```
gym: $ pip3 install gym  
```
EnergyPlus 8.8.0    

### Installation:  
git clone this repository and install  
```
$ cd gym_energyplus  
$ pip install -e .
```
### Usage:
```
import gym
import gym_datacenter
env = gym.make('gym_datacenter:datacenter-v0')  

observation = env.reset()  
action =  env.action_space.sample()   
observation, reward, done, info = env.step(action)  
```
### env Functions:  
```
__init__(self)  
step(self, action)  
reset(self)  
render(self)  
close(self)  
```
