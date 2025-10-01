#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from levha_detection_system.srv import LevhaList
import sys

class LevhaServiceClient(Node):
    def __init__(self):
        super().__init__('levha_service_client')
        self.client = self.create_client(LevhaList, 'levha_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service bekleniyor...")
        self.get_logger().info("Client hazır.")

    def send_request(self, levha_adlari=None, statu=False, confidences=None, xs=None, ys=None):
        if levha_adlari is None:
            levha_adlari = []
        if confidences is None:
            confidences = []
        if xs is None:
            xs = []
        if ys is None:
            ys = []

        req = LevhaList.Request()
        req.levha_adlari = levha_adlari
        req.confidences = confidences
        req.xs = xs
        req.ys = ys
        req.statu = statu

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
                response = node.send_request(statu=False)
                print("Statu False gönderildi, server kapanacak.")
                node.destroy_node()
                rclpy.shutdown()
                sys.exit(0)
            else:
                statu = True

            levha_adlari, confidences, xs, ys = [], [], [], []

            for i in range(adet):
                print(f"\n{i+1}. levha bilgileri:")
                levha_adlari.append(input("Levha adı: "))
                while True:
                    try:
                        confidence = float(input("Confidence değeri (0-100 arasında olmalı): "))
                        if 0 <= confidence <= 100:
                            confidences.append(confidence)
                            break
                        else:
                            print("0-100 arasında olmalı.")
                    except ValueError:
                        print("Geçersiz sayı. Tekrar deneyin.")

                while True:
                    try:
                        xs.append(float(input("X konumu: ")))
                        ys.append(float(input("Y konumu: ")))
                        break
                    except ValueError:
                        print("Geçersiz sayı. Tekrar dene.")

            response = node.send_request(levha_adlari, statu, confidences, xs, ys)
            if response:
                print(f"\nEn yakın levha: {response.en_yakin_levha}")
                print(f"Uzaklık: {response.uzaklik}")
                print(f"Durum: {response.durum}")
            else:
                print("Service'ten cevap alınamadı!")

    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
