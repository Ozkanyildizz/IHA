from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([

        # triangle_service
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'triangle_service_client_package', 'triangle_service'],
            shell=False
        ),

        # triangle_client
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'triangle_service_client_package', 'triangle_client'],
            shell=False
        ),

        # publisher
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'pub_sub_package', 'publisher'],
            shell=False
        ),

        # subscriber
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'pub_sub_package', 'subscriber'],
            shell=False
        ),

        # turtlesim
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'turtlesim', 'turtlesim_node'],
            shell=False
        ),

        # multi_shapes
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'multi_shapes_package', 'multi_shapes'],
            shell=False
        )
    ])

