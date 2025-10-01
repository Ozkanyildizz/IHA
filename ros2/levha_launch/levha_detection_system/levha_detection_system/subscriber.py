#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import sys

class LevhaSubscriber(Node):
    def __init__(self):
        super().__init__('levha_subscriber')
        self.subscription = self.create_subscription(
            String, 'levha_topic', self.listener_callback, 10
        )
        self.get_logger().info("Subscriber hazır, veri bekliyor...")

    def listener_callback(self, msg):
        if msg.data == "kapatılıyor":
            self.get_logger().info("Server kapandı, subscriber kapanıyor...")
            self.destroy_node()
            rclpy.shutdown()
            sys.exit(0)
        else:
            fields = msg.data.split(", ")
            print("+------------------+----------------------+")
            print("|      Field       |      Value           |")
            print("+------------------+----------------------+")
            for field in fields:
                key, value = field.split("=")
                print(f"| {key:<16} | {value:<20} |")
                print("+------------------+----------------------+")

def main(args=None):
    rclpy.init(args=args)
    node = LevhaSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
