# archo

ROS 2 packages for simulating a warehouse robot with SLAM.

<img width="1197" height="755" alt="Screenshot 2026-09-29 at 12 41 38 PM" src="https://github.com/user-attachments/assets/9333e4f6-b73b-44f1-a1ea-7283278cec21" />
<img width="1444" height="680" alt="image" src="https://github.com/user-attachments/assets/7e6ac6ac-3614-4d21-8ea8-b2391312472e" />


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
