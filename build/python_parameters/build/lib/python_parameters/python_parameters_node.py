import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')

        self.declare_parameter('my_parameter', '') # test
        self.declare_parameter('FPS', 20) # test
        self.declare_parameter('pubRate', 20)
        self.declare_parameter('xLims', [1, 1000])
        
        # self.timer = self.create_timer(1, self.timer_callback)

        # UNCOMMENT if you do not need to use a .yaml file
        # self.timer_callback()

    def timer_callback(self):
        # my_param = self.get_parameter('my_parameter').get_parameter_value().string_value
        # self.get_logger().info('Hello %s!' % my_param)

        param_1 = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )

        param_2 = rclpy.parameter.Parameter(
            'FPS',
            rclpy.Parameter.Type.INTEGER,
            15
        )
        
        all_new_parameters = [param_1, param_2]
        self.set_parameters(all_new_parameters)
        print('\nParameters were set!!!\n')

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
