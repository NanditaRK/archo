# archo

ROS 2 packages for simulating a warehouse robot with SLAM.

## Packages

* archo_description - Robot description and simulation files
* archo_slam - SLAM configuration and launch files

## Requirements

* ROS 2 Jazzy

## Installation

```bash
git clone https://github.com/NanditaRK/archo.git
cd archo
colcon build
source install/setup.bash
```

## Usage

```bash
ros2 launch archo_description simulation.launch.py
ros2 launch archo_slam slam.launch.py

# teleop
ros2 launch archo_description teleop.launch.py
```
