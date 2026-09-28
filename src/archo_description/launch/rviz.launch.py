import os

from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command


def generate_launch_description():
    
    package_name = 'archo_description'
    package_share = get_package_share_directory(package_name)
    
    xacro_model = os.path.join(package_share, 'urdf', 'archo.urdf.xacro')
    robot_description = Command(['xacro', ' ', xacro_model])
    rviz_config = os.path.join(package_share, 'rviz', 'archo_robot.rviz')

    robot_state_publisher = Node(package='robot_state_publisher', executable='robot_state_publisher', output='screen', parameters=[{'robot_description': robot_description, 'use_sim_time': True}])
   
#    joint_state_publisher_gui = Node(package='joint_state_publisher_gui', executable='joint_state_publisher_gui', output='screen')
    
    rviz_viewer = Node(package='rviz2', executable='rviz2', output='screen', arguments=['-d', rviz_config], parameters=[{'use_sim_time': True}])

    return LaunchDescription([
        robot_state_publisher,
 #       joint_state_publisher_gui,
        rviz_viewer
    ])
