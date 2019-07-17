A PIP package for building simulation environment. It is build following openai gym interface: https://github.com/openai/gym/blob/master/docs/creating-environments.md   

### Dependences:  
#### python  
version > 3.5  
#### gym  
```
gym: $ pip3 install gym  
```
#### EnergyPlus 8.8.0    
[details on how to install](https://energyplus.net/quickstart#run)

### Installation (Ubuntu 16.04 / Ubuntu 18.04):  
git clone this repository and install  
```
$ pip3 install -e gym_datacenter  
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
