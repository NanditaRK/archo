import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():


    package_name = 'archo_description'
    package_share = get_package_share_directory(package_name)

    xacro_model = os.path.join(
        package_share,
        'urdf',
        'archo.urdf.xacro'
    )

    world_file = os.path.join(
        package_share,
        'worlds',
        'obstacles.sdf'
    )


    robot_description = Command([
        'xacro',
        ' ',
        xacro_model
    ])


    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description,
                'use_sim_time': True
            }
        ]
    )


    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            ])
        ),
        launch_arguments={
            'gz_args': f'-r {world_file}'
        }.items()
    )


    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world',
            'obstacles',
            '-topic',
            'robot_description',
            '-name',
            'archo',
            '-x',
            '0.0',
            '-y',
            '0.0',
            '-z',
            '0.1'
        ],
        output='screen'
    )


    joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'joint_state_broadcaster',
            '--controller-manager',
            '/controller_manager'
        ],
        output='screen'
    )

    diff_drive_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=[
            'diff_drive_controller',
            '--controller-manager',
            '/controller_manager'
        ],
        output='screen'
    )


    #give Gazebo time to start before spawning the robot
    delayed_spawn = TimerAction(
        period=2.0,
        actions=[
            spawn_robot
        ]
    )

    delayed_controllers = TimerAction(
        period=4.0,
        actions=[
            joint_state_broadcaster,
            diff_drive_controller
        ]
    )

    return LaunchDescription([
        robot_state_publisher,
        gazebo,
        delayed_spawn,
        delayed_controllers
    ])
