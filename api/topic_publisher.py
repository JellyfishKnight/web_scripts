from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Float32

class PrintPublisher(Node):
    def __init__(self, name: str = "print_publisher"):
        super().__init__(node_name=name)
        self.publisher_ = self.create_publisher(String, "print", 10)
        self.i = 0

    @property
    def topic(self):
        return "/" + self.publisher_.topic

    def publish_print(self) -> int:
        msg = String()
        msg.data = f"Hello World: {self.i}"
        self.publisher_.publish(msg)
        self.i += 1

        message = f'Message "{msg.data}" published to topic "{self.topic}"'

        return self.i


# def main():
#     rclpy.init()

#     minimal_publisher = PrintPublisher()
#     minimal_publisher.publish_print()

#     minimal_publisher.destroy_node()
#     rclpy.shutdown()


# if __name__ == "__main__":
#     main()