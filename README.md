A PIP package for building simulation environment. It is build following openai gym interface: https://github.com/openai/gym/blob/master/docs/creating-environments.md   

### Dependences:  
#### python  
version >= 3.5  
#### EnergyPlus 8.8.0    
[details on how to install](https://energyplus.net/quickstart#run)
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
In $(HOME)/.bashrc
```
# Specify the top directory
TOP=~/gym_datacenter
export PYTHONPATH=${PYTHONPATH}:${TOP}
MODEL_DIR="${TOP}/EnergyPlus/Model"

if [ `uname` == "Darwin" ]; then
	energyplus_instdir="/Applications"
else
	energyplus_instdir="/usr/local"
fi
ENERGYPLUS_VERSION="8-8-0"
ENERGYPLUS_DIR="${energyplus_instdir}/EnergyPlus-${ENERGYPLUS_VERSION}"
WEATHER_DIR="${ENERGYPLUS_DIR}/WeatherData"
export ENERGYPLUS="${ENERGYPLUS_DIR}/energyplus"

# Weather file.
# Single weather file or multiple weather files separated by comma character.
export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
#export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_CO_Golden-NREL.724666_TMY3.epw"
#export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_FL_Tampa.Intl.AP.722110_TMY3.epw"
#export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw"
#export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_VA_Sterling-Washington.Dulles.Intl.AP.724030_TMY3.epw"
#export ENERGYPLUS_WEATHER="${WEATHER_DIR}/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw,${WEATHER_DIR}/USA_CO_Golden-NREL.724666_TMY3.epw,${WEATHER_DIR}/USA_FL_Tampa.Intl.AP.722110_TMY3.epw"

# Ouput directory "openai-YYYY-MM-DD-HH-MM-SS-mmmmmm" is created in
# the directory specified by ENERGYPLUS_LOGBASE or in the current directory if not specified.
export ENERGYPLUS_LOGBASE="${HOME}/eplog"

# Model file. Uncomment one.
#export ENERGYPLUS_MODEL="${MODEL_DIR}/2ZoneDataCenterHVAC_wEconomizer_Temp.idf"     # Temp. setpoint control
export ENERGYPLUS_MODEL="${MODEL_DIR}/2ZoneDataCenterHVAC_wEconomizer_Temp_Fan.idf" # Temp. setpoint and fan control

# Run command (example)
# $ time python3 -m baselines_energyplus.trpo_mpi.run_energyplus --num-timesteps 1000000000

# Monitoring (example)
# $ python3 -m baselines_energyplus.common.plot_energyplus
```

#### gym  
```
gym: $ pip3 install gym  
```
#### other packages
```
pip3 install tensorflow  
pip3 install troch  
pip3 install pandas 
```

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
