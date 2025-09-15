#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from levha_detection_system.srv import LevhaList

class LevhaServiceClient(Node):
    def __init__(self):
        super().__init__('levha_service_client')
        self.client = self.create_client(LevhaList, 'levha_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service bekleniyor...")

    def send_request(self, levha_adlari, confidences, xs, ys):
        req = LevhaList.Request()
        req.levha_adlari = levha_adlari
        req.confidences = confidences
        req.xs = xs
        req.ys = ys

        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    node = LevhaServiceClient()

    try:
        while True:
            try:
                adet = int(input("Kaç adet levha tanımlamak istiyorsunuz? (0 ile çıkış): "))
            except ValueError:
                print("Geçersiz sayı. Tekrar deneyin.")
                continue

            if adet == 0:
                break

            levha_adlari = []
            confidences = []
            xs = []
            ys = []

            for i in range(adet):
                print(f"\n{i+1}. levha bilgileri:")
                levha_adlari.append(input("Levha adı: "))
                confidences.append(float(input("Confidence değeri: ")))
                xs.append(float(input("X konumu: ")))
                ys.append(float(input("Y konumu: ")))

            response = node.send_request(levha_adlari, confidences, xs, ys)
            print(f"\nEn yakın levha: {response.en_yakin_levha}")
            print(f"Uzaklık: {response.uzaklik}")
            print(f"Durum: {response.durum}")
    finally:
        rclpy.shutdown()
if __name__ == '__main__':
    main()