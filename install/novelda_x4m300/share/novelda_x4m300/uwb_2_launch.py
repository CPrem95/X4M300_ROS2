from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    radar2 = '/dev/ttyACM1'

    topic2 = '/UWBradar2/readings'

    # creates the path to the YAML file
    config = os.path.join(
        get_package_share_directory('novelda_x4m300'),
        'config',
        'params.yaml'
        )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'd2',
            default_value=radar2,
            description='Specify the device address of radar #2'
        ),

        DeclareLaunchArgument(
            'config_file',
            default_value=config,
            description='Path to the YAML configuration file'
        ),

        DeclareLaunchArgument(
            't2',
            default_value=topic2,
            description='Specify the topic of radar #1 obs'
        ),

        # Parameters node
        Node(
            package='python_parameters',
            namespace='myParams',
            executable='param_node',
            name='vals',
            parameters=[LaunchConfiguration('config_file')],
        ),

        # UWB Radar nodes. Comment unused nodes
        Node(
            package='novelda_x4m300',
            namespace='UWBradar2',
            executable='uwbTalker',
            name='obs',
            arguments=['-d', LaunchConfiguration('d2')],
            parameters=[LaunchConfiguration('config_file')],
            output='screen'
        ),
        
        # Plotting nodes for each radar
        Node(
            package='novelda_x4m300',
            namespace='UWBplot2',
            executable='uwbListener',
            name='plt',
            arguments=['-t', LaunchConfiguration('t2')],
            output='screen'
        )
    ])
