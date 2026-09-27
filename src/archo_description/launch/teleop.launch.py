from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    teleop = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        prefix='xterm -e',
        output='screen',
        parameters=[
            {
                'stamped': True
            }
        ],
        remappings=[
            (
                '/cmd_vel',
                '/diff_drive_controller/cmd_vel'
            )
        ]
    )

    return LaunchDescription([
        teleop
    ])
