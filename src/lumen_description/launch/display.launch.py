
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    LaunchConfiguration,
    Command,
    PathJoinSubstitution,
    FindExecutable
)

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    package_name = 'lumen_description'

    xacro_file = PathJoinSubstitution([
        FindPackageShare(package_name),
        'urdf',
        'lumen.urdf.xacro'
    ])

    rviz_config_file = PathJoinSubstitution([
        FindPackageShare(package_name),
        'rviz',
        'lumen.rviz'
    ])

    use_sim_time = LaunchConfiguration('use_sim_time')

    robot_description = Command([
        FindExecutable(name='xacro'),
        ' ',
        xacro_file
    ])

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': use_sim_time
        }]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false'
        ),
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])
