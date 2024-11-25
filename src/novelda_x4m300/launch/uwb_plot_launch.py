from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    topic0 = '/UWBradar1/readings'

    # creates the path to the YAML file
    config = os.path.join(
        get_package_share_directory('novelda_x4m300'),
        'config',
        'params.yaml'
        )

    return LaunchDescription([

        DeclareLaunchArgument(
            'config_file',
            default_value=config,
            description='Path to the YAML configuration file'
        ),

        DeclareLaunchArgument(
            't1',
            default_value=topic0,
            description='Specify the topic of radar #1 obs'
        ),

        # Plotting nodes for each radar
        Node(
            package='novelda_x4m300',
            namespace='UWBplot0',
            executable='uwbListener',
            # name='plot',
            arguments=['-t', LaunchConfiguration('t1')],
            parameters=[LaunchConfiguration('config_file')],
            output='screen'
        ),
    ])