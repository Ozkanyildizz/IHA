import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time
import os
import threading

class ShapeDrawer(Node):
    def __init__(self):
        super().__init__('shape_drawer')
        self.pub_dict = {}
        turtles = ["turtle1", "turtle2", "turtle3", "turtle4", "turtle5"]
        for t in turtles:
            self.pub_dict[t] = self.create_publisher(Twist, f'/{t}/cmd_vel', 10)

    def move(self, turtle, linear, angular, duration):
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        pub = self.pub_dict[turtle]
        end_time = time.time() + duration
        while time.time() < end_time:
            pub.publish(msg)
            time.sleep(0.05)   # daha akıcı hareket
        # durdur
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        pub.publish(msg)

    def draw_polygon(self, turtle, sides, length=2.0, speed=1.0):
        # Her kenarın uzunluğu için düz git
        # sonra dış açıya dön
    	
        angle = (2 * math.pi) / sides  
        for _ in range(sides):
        # ileri git
            self.move(turtle, speed, 0.0, length/speed)
        # dış açı kadar dön
            self.move(turtle, 0.0, speed, angle/speed)


    def draw_star(self, turtle, length=2.0, speed=1.0):
        turn_speed = 1.5
        for _ in range(5):
            self.move(turtle, speed, 0.0, length/speed)
            self.move(turtle, 0.0, turn_speed, (4*math.pi/5)/turn_speed)

def main(args=None):
    rclpy.init(args=args)
    node = ShapeDrawer()

    # Turtle spawn - hepsini farklı yerlere koy
    os.system("ros2 service call /spawn turtlesim/srv/Spawn \"{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}\"")
    os.system("ros2 service call /spawn turtlesim/srv/Spawn \"{x: 8.0, y: 8.0, theta: 0.0, name: 'turtle3'}\"")
    os.system("ros2 service call /spawn turtlesim/srv/Spawn \"{x: 2.0, y: 6.0, theta: 0.0, name: 'turtle4'}\"")
    os.system("ros2 service call /spawn turtlesim/srv/Spawn \"{x: 8.0, y: 1.0, theta: 0.0, name: 'turtle5'}\"")

    time.sleep(2)  # spawn için bekle

    # Her turtle için thread başlat -> aynı anda çizecekler
    threads = []
    threads.append(threading.Thread(target=node.draw_star, args=("turtle1",)))
    threads.append(threading.Thread(target=node.draw_polygon, args=("turtle2", 3)))
    threads.append(threading.Thread(target=node.draw_polygon, args=("turtle3", 4)))
    threads.append(threading.Thread(target=node.draw_polygon, args=("turtle4", 5)))
    threads.append(threading.Thread(target=node.draw_polygon, args=("turtle5", 6)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    rclpy.shutdown()

if __name__ == '__main__':
    main()

