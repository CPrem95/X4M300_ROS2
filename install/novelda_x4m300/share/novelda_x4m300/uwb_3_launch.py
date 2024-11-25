from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    radar3 = '/dev/ttyACM2'

    topic3 = '/UWBradar3/readings'

    # creates the path to the YAML file
    config = os.path.join(
        get_package_share_directory('novelda_x4m300'),
        'config',
        'params.yaml'
        )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'd3',
            default_value=radar3,
            description='Specify the device address of radar #3'
        ),

        DeclareLaunchArgument(
            'config_file',
            default_value=config,
            description='Path to the YAML configuration file'
        ),
        
        # UWB Radar nodes. Comment unused nodes
        Node(
            package='novelda_x4m300',
            namespace='UWBradar3',
            executable='uwbTalker',
            name='read',
            arguments=['-d', LaunchConfiguration('d3')],
            parameters=[LaunchConfiguration('config_file')],
            output='screen'
        ),
        
        # Plotting nodes for each radar
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBplot3',
        #     executable='uwbListener',
        #     name='plt',
        #     arguments=['-t', LaunchConfiguration('t3')],
        #     output='screen'
        # )
    ])
