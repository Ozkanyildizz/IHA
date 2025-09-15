#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LevhaSubscriber(Node):
    def __init__(self):
        super().__init__('levha_subscriber')
        self.subscription = self.create_subscription(
            String, 'levha_topic', self.listener_callback, 10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"En yakın levha bilgisi: {msg.data}")
        print("+------------------+----------------------+")
        print("|      Field       |      Value           |")
        print("+------------------+----------------------+")
        print(msg.data.split(", ")[0].split("=")[0], "             |", end=" ")
        print(msg.data.split(", ")[0].split("=")[1])
        print("+------------------+----------------------+")
        print(msg.data.split(", ")[1].split("=")[0], "              |", end=" ")
        print(msg.data.split(", ")[1].split("=")[1])
        print("+------------------+----------------------+")
        print(msg.data.split(", ")[2].split("=")[0], "             |", end=" ")
        print(msg.data.split(", ")[2].split("=")[1])
        print("+------------------+----------------------+")
        print(msg.data.split(", ")[3].split("=")[0], "        |", end=" ")
        print(msg.data.split(", ")[3].split("=")[1])
        print("+------------------+----------------------+")
        print(msg.data.split(", ")[4].split("=")[0], "           |", end=" ")
        print(msg.data.split(", ")[4].split("=")[1])
        print("+------------------+----------------------+")
        print(msg.data.split(", ")[5].split("=")[0], "             |",  end=" ")
        print(msg.data.split(", ")[5].split("=")[1])

def main(args=None):
    rclpy.init(args=args)
    node = LevhaSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == '__main__':
    main()
