from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='occupancy_grid_demo',
            executable='occupancy_grid_publisher',
            name='occupancy_grid_publisher',
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            output='screen',
            arguments=[
                '-entity', 'holonomic_robot',
                '-file', '/home/deylahm/Desktop/Simulacion Rotbot/Prueba-Ros2/install/holonomic_robot/share/holonomic_robot/urdf/holonomic_robot.urdf'
            ]
        ),
        Node(
            package='gazebo_ros',
            executable='gazebo',
            name='gazebo',
            output='screen',
            arguments=[
                '--verbose',
                '-s', 'libgazebo_ros_init.so',
                '-s', 'libgazebo_ros_factory.so'
            ]
        )
    ])
