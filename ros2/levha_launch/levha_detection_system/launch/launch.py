from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'bash', '-lc',
                 'source /opt/ros/foxy/setup.bash; source /home/ozkan/ros2_ws/install/setup.bash; ros2 run levha_detection_system server.py; exec bash'],
            shell=False
        ),
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'bash', '-lc',
                 'source /opt/ros/foxy/setup.bash; source /home/ozkan/ros2_ws/install/setup.bash; ros2 run levha_detection_system client.py; exec bash'],
            shell=False
        ),
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'bash', '-lc',
                 'source /opt/ros/foxy/setup.bash; source /home/ozkan/ros2_ws/install/setup.bash; ros2 run levha_detection_system subscriber.py; exec bash'],
            shell=False
        ),
    ])
