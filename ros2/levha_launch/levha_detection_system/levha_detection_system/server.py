#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from levha_detection_system.srv import LevhaList
from levha_detection_system import utils
from std_msgs.msg import String
from datetime import datetime
import math
import sys

class LevhaServiceServer(Node):
    def __init__(self):
        super().__init__('levha_service_server')
        self.srv = self.create_service(LevhaList, 'levha_service', self.check)
        self.publisher = self.create_publisher(String, 'levha_topic', 10)
        self.get_logger().info("Server hazır, veri bekliyor...")

    def check(self, request, response):
        if not request.statu:
            self.get_logger().info("Statu False, node kapanıyor...")
            response.en_yakin_levha = ""
            response.uzaklik = 0.0
            response.durum = "İşlem yapılmadı"

            msg = String()
            msg.data = "kapatılıyor"
            self.publisher.publish(msg)

            self.destroy_node()
            sys.exit(0)
        else:
            return self.callback(request, response)

    def callback(self, request, response):
        min_distance = float('inf')
        en_yakin_index = 0

        if len(request.xs) > 1:
            for i, (x, y) in enumerate(zip(request.xs, request.ys)):
                uzaklik = math.sqrt(x**2 + y**2)
                if uzaklik < min_distance:
                    min_distance = uzaklik
                    en_yakin_index = i

        levha_adi = request.levha_adlari[en_yakin_index]
        confidence = request.confidences[en_yakin_index]
        uzaklik = math.sqrt(request.xs[en_yakin_index]**2 + request.ys[en_yakin_index]**2)

        if confidence >= 95:
            durum = "Tespit edildi"
        elif 85 <= confidence < 95:
            durum = "Tespit edildi net değil!"
        else:
            durum = "İşleme alınamadı"

        utils.kayit_ekle(levha_adi, confidence, uzaklik, durum)

        now = datetime.now()
        msg = String()
        msg.data = (
            f"tarih={now.strftime('%Y-%m-%d')}, saat={now.strftime('%H:%M:%S')}, "
            f"levha={levha_adi}, confidence={confidence}, uzaklik={uzaklik:.2f}, durum={durum}"
        )
        self.publisher.publish(msg)
        print(f"En yakın levha bilgisi: {msg.data}")

        response.en_yakin_levha = levha_adi
        response.uzaklik = uzaklik
        response.durum = durum
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LevhaServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
