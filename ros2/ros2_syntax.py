import rclpy                       # ROS2 Python client library
from rclpy.node import Node        # Node sınıfı (her node bundan türetilir)

# 1. Node sınıfı
class MyNode(Node):
    def __init__(self):
        super().__init__('my_node_name')   # Node adı (ROS graph’ta görünür)

        # Örnek: Publisher oluştur
        self.publisher_ = self.create_publisher(
            String,       # Mesaj tipi
            'topic',      # Topic adı
            10            # QoS queue size
        )

        # Örnek: Subscriber oluştur
        self.subscription = self.create_subscription(
            String,       # Mesaj tipi
            'topic',
            self.listener_callback,   # Callback fonksiyon
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Subscription: {msg.data}')


# 2. main() fonksiyonu → entry point burayı çağırır
def main(args=None):
    rclpy.init(args=args)             # ROS2 başlat
    node = MyNode()                   # Node nesnesi oluştur
    rclpy.spin(node)                  # Node’u çalıştır (dinlemeye devam et)
    node.destroy_node()               # Temizlik
    rclpy.shutdown()                  # ROS2 kapat


# Eğer direkt çalıştırırsan python3 dosya.py → çalışsın diye
if __name__ == '__main__':
    main()

