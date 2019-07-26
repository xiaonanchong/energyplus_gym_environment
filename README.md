A PIP package for building simulation environment. It is build following openai gym interface: https://github.com/openai/gym/blob/master/docs/creating-environments.md   

### Dependences:  
#### python  
version >= 3.5  
#### EnergyPlus 8.8.0  
```
$ wget https://github.com/NREL/EnergyPlus/archive/v8.8.0.zip    
$ unzip v8.8.0.zip  
$ cd <WORKING-DIRECTORY>/EnergyPlus  
$ patch -p1 < ../gym_datacenter/RL-patch-for-EnergyPlus-8-8-0.patch  
$ mkdir build   
$ cd build   
$ cmake -DCMAKE_INSTALL_PREFIX=/usr/local/EnergyPlus-8-8-0 ..  
$ make -j4  
$ sudo make install  
```
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
