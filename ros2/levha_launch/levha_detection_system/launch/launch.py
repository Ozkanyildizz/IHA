from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='levha_detection_system',
            executable='server.py',
            name='levha_server',
            output='screen',
            prefix="gnome-terminal -- bash -c"
        ),
        Node(
            package='levha_detection_system',
            executable='client.py',
            name='levha_client',
            output='screen',
            prefix="gnome-terminal -- bash -c"
        ),
        Node(
            package='levha_detection_system',
            executable='subscriber.py',
            name='levha_subscriber',
            output='screen',
            prefix="gnome-terminal -- bash -c"
        ),
    ])
