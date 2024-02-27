from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    radar1 = '/dev/ttyACM0'
    radar2 = '/dev/ttyACM1'
    radar3 = '/dev/ttyACM2'
    radar4 = '/dev/ttyACM3'

    return LaunchDescription([
        DeclareLaunchArgument(
            'd1',
            default_value=radar1,
            description='Specify the device address of radar #1'
        ),
        DeclareLaunchArgument(
            'd2',
            default_value=radar2,
            description='Specify the device address of radar #2'
        ),
        DeclareLaunchArgument(
            'd3',
            default_value=radar3,
            description='Specify the device address of radar #3'
        ),
        DeclareLaunchArgument(
            'd4',
            default_value=radar4,
            description='Specify the device address of radar #4'
        ),


        Node(
            package='novelda_x4m300',
            namespace='UWBradar1',
            executable='uwbTalker',
            name='sim',
            # parameters=[{'d': LaunchConfiguration('d1')}]
        ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBradar2',
        #     executable='uwbTalker',
        #     name='sim',
        #     parameters=[{'d': 'd2'}]
        # ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBradar3',
        #     executable='uwbTalker',
        #     name='sim',
        #     parameters=[{'d': 'd3'}]
        # ),
        # Node(
        #     package='novelda_x4m300',
        #     namespace='UWBradar4',
        #     executable='uwbTalker',
        #     name='sim',
        #     parameters=[{'d': 'd4'}]
        # ),
        




        # Node(
        #     package='turtlesim',
        #     executable='mimic',
        #     name='mimic',
        #     remappings=[
        #         ('/input/pose', '/turtlesim1/turtle1/pose'),
        #         ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
        #     ]
        # )
    ])