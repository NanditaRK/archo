import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'archo_slam'

    package_share = get_package_share_directory(package_name)

    slam_params_file = os.path.join(
        package_share,
        'config',
        'slam_toolbox.yaml'
    )

    slam_toolbox = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
            slam_params_file,
            {
                'use_sim_time': True
            }
        ]
    )

    return LaunchDescription([
        slam_toolbox
    ])
