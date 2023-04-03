#!/usr/bin/env python3

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    default_config_topics = os.path.join(get_package_share_directory('husky_teleop'),
                                         'config', 'twist_mux_topics.yaml')
    return LaunchDescription([
        DeclareLaunchArgument(
            'config_topics',
            default_value=default_config_topics,
            description='Default topics config file'),
        Node(
            package='twist_mux',
            executable='twist_mux',
            output='screen',
            remappings={('/cmd_vel_out', '/husky_velocity_controller/cmd_vel_unstamped')},
            parameters=[LaunchConfiguration('config_topics')]
        )])

