from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    radar1 = '/dev/ttyACM1'
    # radar2 = '/dev/ttyACM2'
    # radar3 = '/dev/ttyACM3'
    # radar4 = '/dev/ttyACM4'

    topic1 = '/UWBradar1/readings'
    # topic2 = '/UWBradar2/readings'
    # topic3 = '/UWBradar3/readings'
    # topic4 = '/UWBradar4/readings'

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
        # DeclareLaunchArgument(
        #     'd2',
        #     default_value=radar2,
        #     description='Specify the device address of radar #2'
        # ),
        # DeclareLaunchArgument(
        #     'd3',
        #     default_value=radar3,
        #     description='Specify the device address of radar #3'
        # ),
        # DeclareLaunchArgument(
        #     'd4',
        #     default_value=radar4,
        #     description='Specify the device address of radar #4'
        # ),

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
        # DeclareLaunchArgument(
        #     't2',
        #     default_value=topic2,
        #     description='Specify the topic of radar #1 obs'
        # ),

        # Parameters node
        Node(
            package='python_parameters',
            namespace='myParams',
            executable='param_node',
            name='vals',
            parameters=[LaunchConfiguration('config_file'), '--ros-args', '--log-level', 'error'],
        ),

        # UWB Radar nodes. Comment unused nodes
        Node(
            package='novelda_x4m300',
            namespace='UWBradar1',
            executable='uwbTalker',
            name='obs',
            arguments=['-d', LaunchConfiguration('d1'), '--ros-args', '--log-level', 'error'],
            parameters=[LaunchConfiguration('config_file')],
            output='screen'
        ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBradar2',
        #     executable='uwbTalker',
        #     name='obs',
        #     arguments=['-d', LaunchConfiguration('d2')],
        #     parameters=[LaunchConfiguration('config_file')],
        #     output='screen'
        # ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBradar3',
        #     executable='uwbTalker',
        #     name='obs',
        #     arguments=['-d', LaunchConfiguration('d3')],
        #     parameters=[LaunchConfiguration('config_file')],
        #     output='screen'
        # ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBradar4',
        #     executable='uwbTalker',
        #     name='obs',
        #     arguments=['-d', LaunchConfiguration('d4')],
        #     parameters=[LaunchConfiguration('config_file')],
        #     output='screen'
        # ),
        
        # Plotting nodes for each radar
        Node(
            package='novelda_x4m300',
            namespace='UWBplot1',
            executable='uwbListener',
            name='plt',
            arguments=['-t', LaunchConfiguration('t1')],
            # parameters=[LaunchConfiguration('config_file')],
            output='screen'
        ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBplot2',
        #     executable='uwbListener',
        #     name='plt',
        #     arguments=['-t', LaunchConfiguration('t2')],
        #     output='screen'
        # ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBplot3',
        #     executable='uwbListener',
        #     name='plt',
        #     arguments=['-t', LaunchConfiguration('t3')],
        #     output='screen'
        # ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBplot4',
        #     executable='uwbListener',
        #     name='plt',
        #     arguments=['-t', LaunchConfiguration('t4')],
        #     output='screen'
        # )
    ])
