from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Obtiene el directorio de instalación del paquete
    package_share_directory = os.path.join(
        os.getenv('AMENT_PREFIX_PATH').split(':')[0],
        'share/holonomic_robot'
    )

    # Construye la ruta al archivo URDF
    urdf_file = os.path.join(package_share_directory, 'urdf', 'holonomic_robot.urdf')
    
    # Construye la ruta al archivo de configuración de RViz
    # Subir tres niveles desde launch para llegar a la raíz del proyecto
    rviz_config_file = os.path.join(
        os.getenv('AMENT_PREFIX_PATH').split(':')[0], 
        'default.rviz'
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'holonomic_robot', '-file', urdf_file],
            output='screen'
        ),
        Node(
            package='holonomic_robot',
            executable='occupancy_grid_publisher',
            name='occupancy_grid_publisher',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file']
        )
    ])
