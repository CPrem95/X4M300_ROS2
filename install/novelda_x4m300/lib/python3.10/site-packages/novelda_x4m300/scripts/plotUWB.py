#!/usr/bin/env python3

from novelda_x4m300.scripts.python35.pymoduleconnector.rawreadings import *
from optparse import OptionParser
import rclpy
from rclpy.node import Node
# from custom_interfaces.msg import FloatList
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from std_msgs.msg import Float32MultiArray
import threading
from ament_index_python.packages import get_package_share_directory
import os
import yaml

class Visualiser(Node):
    def __init__(self, topic_name):
        super().__init__('UWBlistener')

        ''' NOT WORKING AS EXPECTED
        self.declare_parameter('xLims', [1,700])  # plot limits
        self.xlims =  self.get_parameter('xLims').get_parameter_value().integer_array_value

        self.declare_parameter('bins', 700)  # number of bins
        self.bins =  self.get_parameter('bins').get_parameter_value().integer_value

        self.get_logger().info("xLims: %s" % self.xlims)
        self.get_logger().info("bins: %s" % self.bins)
        '''
        yaml_file = os.path.join(
            get_package_share_directory('novelda_x4m300'),
            'config',
            'params.yaml'
            )

        # Open and read the YAML file
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            
        self.xlims = data["UWBplot0"]["UWBlistener"]["ros__parameters"]["xLims"]

        self.get_logger().info("xLims: %s" % self.xlims)

        self.fig, self.ax = plt.subplots()
        self.fig.suptitle(topic_name)
        plt.ylabel("normalized amplitudes")
        plt.xlabel("bins")
        plt.grid()
        self.ln, = plt.plot([], [], linewidth=0.5, color='b')
        self.x_data, self.y_data = [] , []

        self.subscription = self.create_subscription(
            Float32MultiArray,
            topic_name,
            self.UWBcallback,
            2
        )
        self.subscription

        

    def plot_init(self):
        self.ax.set_xlim(self.xlims[0], self.xlims[1])
        self.ax.set_ylim(-0.03, 0.03)
        return self.ln

    def UWBcallback(self, msg):
        frame = msg.data
        self.y_data = frame[self.xlims[0]:self.xlims[1]]
        self.x_data = range(self.xlims[0], self.xlims[1])
    
    def update_plot(self, frame):
        self.ln.set_data(self.x_data, self.y_data)
        return self.ln

def main(args = None):

    parser = OptionParser()
    parser.add_option(
        "-t",
        "--topic",
        dest="topic_name",
        help="topic to use")
    
    parser.add_option(
        "--ros-args",
        dest="NA1",
        help="ROS2 passes all these commands which will cause errors, so had to mention here")
    
    parser.add_option(
        "-r",
        dest="NA2",
        help="ROS2 passes all these commands which will cause errors, so had to mention here")
    
    parser.add_option(
        "--params-file",
        dest="NA3",
        help="ROS2 passes all these commands which will cause errors, so had to mention here")
    
    (options, args) = parser.parse_args()

    rclpy.init(args=args)
    print("\nWaiting for plotting...")
    vis = Visualiser(options.topic_name)
    
    def spin_thread():
        rclpy.spin(vis)

    if not options.topic_name:
            parser.error("Missing -d See --help.")
    else:
        try:
            ani = FuncAnimation(vis.fig, vis.update_plot, init_func=vis.plot_init)

            spin_thread = threading.Thread(target=spin_thread)
            spin_thread.start()

            plt.show(block=True)
                        
        except KeyboardInterrupt:
            spin_thread.join()
            plt.close('all')
            print('Thanks for plotting')
            vis.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()
