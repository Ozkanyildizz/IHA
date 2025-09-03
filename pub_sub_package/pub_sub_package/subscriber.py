import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10
        )
        self.subscription  # ROS2 gerektiriyor
        self.numbers = []

 
    def control(self):
        even_number= 0
        total = 0
        average = 0
        for i in self.numbers:
            if i % 2 == 0:
                even_number +=1
            total += i
        average = total / len(self.numbers) if self.numbers else 0 # zero division error
        return f"{self.numbers}: {even_number} numbers is even, total is {total}, and average is {average}."


    def listener_callback(self, msg):
        # String'i int listesine çevir
        self.numbers = list(map(int, msg.data.split()))
        
        self.get_logger().info(self.control())

def main(args=None):
    rclpy.init(args=args)
    node = MinimalSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

