#!/usr/bin/env python3

from novelda_x4m300.scripts.python35.pymoduleconnector.rawreadings import *
from novelda_x4m300.scripts.python35.pymoduleconnector.moduleconnectorwrapper import *
from optparse import OptionParser
import rclpy
from rclpy.node import Node
from custom_interfaces.msg import FloatList
from std_msgs.msg import Float32MultiArray

class UWBPublisher(Node):

    def __init__(self, dev_name):
        super().__init__('UWBtalker') # calls the Node class constructor and gives the node name
        self.publisher_ = self.create_publisher(Float32MultiArray, 'readings', 2) # queue size = 2

        self.get_device(dev_name)
        self.data2send = Float32MultiArray()

        self.declare_parameter('pubRate', 20) 
        rate =  self.get_parameter('pubRate').get_parameter_value().integer_value

        self.declare_parameter('bins', rclpy.Parameter.Type.INTEGER) 
        self.bins =  self.get_parameter('bins').get_parameter_value().integer_value # length of data to be sent

        self.get_logger().info("bins: %s" % self.bins)
        self.get_logger().info("pubRate: %s" % rate)

        rate = 1/rate # Publishing time period = 1/frequency
        print('\nStarted publishing data...! ' + dev_name)
        clear_buffer(self.xep)
        self.timer = self.create_timer(rate, self.timer_callback)

    def get_device(self, dev_name):
        self.device = dev_name
        self.xep, self.mc = configure(self.device)
            
    def timer_callback(self):

        clear_buffer(self.xep)
        frame = read_frame(self.xep)
        # rospy.loginfo(frame)
        self.data2send.data = list(frame[0:self.bins])
        self.publisher_.publish(self.data2send)

def main(args = None):
    print("\nWaiting for UWB...")

    parser = OptionParser()
    parser.add_option(
        "-d",
        "--device",
        dest="device_name",
        help="device file to use")
    
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
    
    rclpy.init(args=args)
    (options, args) = parser.parse_args()

    try:
        uwb = UWBPublisher(options.device_name)
        rclpy.spin(uwb)
    except KeyboardInterrupt:
        print("Interrupted")

    # Stop streaming of data
    print("Stopping UWB...")
    uwb.xep.x4driver_set_fps(0)
    uwb.mc.close()
    uwb.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
