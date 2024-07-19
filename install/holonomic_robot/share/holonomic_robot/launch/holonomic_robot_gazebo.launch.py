from launch import LaunchDescription 

from launch_ros.actions import Node 

from launch.actions import ExecuteProcess 

import os 

 

def generate_launch_description(): 

    package_share_directory = os.path.join( 

        os.getenv('AMENT_PREFIX_PATH').split(':')[0], 

        'share/holonomic_robot' 

    ) 

 

    urdf_file = os.path.join(package_share_directory, 'urdf', 'holonomic_robot.urdf') 

 

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

            package='your_package', 

            executable='occupancy_grid_publisher', 

            name='occupancy_grid_publisher', 

            output='screen' 

        ), 

        Node( 

            package='rviz2', 

            executable='rviz2', 

            name='rviz2', 

            output='screen', 

            arguments=['-d', '/path/to/your/rviz/config/file.rviz'] 

        ) 

    ])