import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        # --- Task 3: Parameters ---
        self.declare_parameter('student_name', 'not set')
        name_param = self.get_parameter('student_name').get_parameter_value().string_value
        
        # --- Task 2: Counter logic ---
        self.file_path = os.path.expanduser('~/ros2_ws/src/my_first_pkg/counter.txt')
        count = self.get_and_update_count()
        
        # --- Outputs ---
        self.get_logger().info('Welcome to Mobile Robotics Lab')
        self.get_logger().info(f'Run count: {count}')
        
        if name_param == 'not set':
            self.get_logger().info('student_name not set')
        else:
            self.get_logger().info(f'Student Name: {name_param}')

    def get_and_update_count(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    count = int(f.read().strip())
                except ValueError:
                    count = 0
        else:
            count = 0
        count += 1
        with open(self.file_path, 'w') as f:
            f.write(str(count))
        return count

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
