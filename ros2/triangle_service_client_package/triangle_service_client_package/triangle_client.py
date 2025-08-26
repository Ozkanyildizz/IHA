#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from triangle_service_client_package.srv import TriangleCalc

class TriangleClient(Node):
    def __init__(self):
        super().__init__('triangle_client')
        self.cli = self.create_client(TriangleCalc, 'triangle_calc')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Servis bekleniyor...')

    def send_request(self, calc_type, a, b, c=0.0):
        req = TriangleCalc.Request()
        req.calc_type = calc_type
        req.a = a
        req.b = b
        req.c = c
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    node = TriangleClient()

    while True:
        print("\n--- Üçgen Hesaplama Menüsü ---")
        print("1. Alan Hesapla")
        print("2. Çevre Hesapla")
        print("3. Çıkış")
        choice = input("Seçiminiz (1/2/3): ")

        if choice == "1":
            a = float(input("Taban uzunluğunu girin: "))
            b = float(input("Yüksekliği girin: "))
            result = node.send_request("alan", a, b)
            print(f"[Servis Cevabı] {result.message}")

        elif choice == "2":
            a = float(input("Kenar 1: "))
            b = float(input("Kenar 2: "))
            c = float(input("Kenar 3: "))
            result = node.send_request("cevre", a, b, c)
            print(f"[Servis Cevabı] {result.message}")

        elif choice == "3":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Hatalı seçim! Tekrar deneyin.")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
