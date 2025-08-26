#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from triangle_service_client_package.srv import TriangleCalc

class TriangleService(Node):
    def __init__(self):
        super().__init__('triangle_service')
        self.srv = self.create_service(
            TriangleCalc,
            'triangle_calc',
            self.handle_triangle
        )

    def handle_triangle(self, request, response):
        if request.calc_type.lower() == "alan":
            response.result = (request.a * request.b) / 2
            response.message = f"Alan: {response.result}"
        elif request.calc_type.lower() == "cevre":
            a, b, c = request.a, request.b, request.c
            if a + b > c and a + c > b and b + c > a:
                response.result = a + b + c
                response.message = f"Çevre: {response.result}"
            else:
                response.result = 0.0
                response.message = "Geçerli üçgen değil!"
        else:
            response.result = 0.0
            response.message = "Hatalı seçim!"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = TriangleService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
