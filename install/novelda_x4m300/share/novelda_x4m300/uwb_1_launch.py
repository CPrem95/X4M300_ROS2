from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    radar1 = '/dev/ttyACM0'

    topic1 = '/UWBradar1/readings'

    # creates the path to the YAML file
    config = os.path.join(
        get_package_share_directory('novelda_x4m300'),
        'config',
        'params.yaml'
        )

    return LaunchDescription([
        DeclareLaunchArgument(
            'd1',
            default_value=radar1,
            description='Specify the device address of radar #1',
        ),

        DeclareLaunchArgument(
            'config_file',
            default_value=config,
            description='Path to the YAML configuration file'
        ),

        DeclareLaunchArgument(
            't1',
            default_value=topic1,
            description='Specify the topic of radar #1 obs'
        ),
        
        # # Parameters node
        # Node(
        #     package='python_parameters',
        #     namespace='myParams',
        #     executable='param_node',
        #     name='vals',
        #     parameters=[LaunchConfiguration('config_file')],
        # ),

        # UWB Radar nodes. Comment unused nodes
        Node(
            package='novelda_x4m300',
            namespace='UWBradar1',
            executable='uwbTalker',
            name='read',
            arguments=['-d', LaunchConfiguration('d1'), '--ros-args', '--log-level', 'error'],
            parameters=[LaunchConfiguration('config_file')],
            output='screen'
        ),
        
        # Plotting nodes for each radar
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBplot1',
        #     executable='uwbListener',
        #     name='plt',
        #     arguments=['-t', LaunchConfiguration('t1')],
        #     # parameters=[LaunchConfiguration('config_file')],
        #     output='screen'
        # ),
        
    ])
