#!/usr/bin/env python3 

  

import rclpy 

from rclpy.node import Node 

from nav_msgs.msg import OccupancyGrid 

from std_msgs.msg import Header 

from geometry_msgs.msg import Pose 

  

class OccupancyGridPublisher(Node): 

    def __init__(self): 

        super().__init__('occupancy_grid_publisher') 

        self.publisher_ = self.create_publisher(OccupancyGrid, 'occupancy_grid', 10) 

        timer_period = 1  # seconds 

        self.timer = self.create_timer(timer_period, self.publish_occupancy_grid) 

        self.occupancy_grid = self.create_occupancy_grid() 

  

    def create_occupancy_grid(self): 

        grid = OccupancyGrid() 

        grid.header = Header() 

        grid.header.frame_id = 'map' 

        grid.info.resolution = 0.1  # Each cell is 10cm x 10cm 

        grid.info.width = 100 

        grid.info.height = 100 

        grid.info.origin = Pose() 

        grid.info.origin.position.x = 0.0 

        grid.info.origin.position.y = 0.0 

        grid.info.origin.position.z = 0.0 

  

        # Initialize grid cells with -1 (unknown) 

        grid.data = [-1] * (grid.info.width * grid.info.height) 
        
        

  

        # Mark some cells as free (0) or occupied (100) 

        grid.data[22] = 100  # Occupied cell 

        grid.data[23] = 100  # Occupied cell 

        grid.data[24] = 100  # Occupied cell 

        grid.data[32] = 0    # Free cell 

        grid.data[33] = 0    # Free cell 

        grid.data[34] = 0    # Free cell 

  

        return grid 

  

    def publish_occupancy_grid(self): 

        self.occupancy_grid.header.stamp = self.get_clock().now().to_msg() 

        self.publisher_.publish(self.occupancy_grid) 

  

  

def main(args=None): 

    rclpy.init(args=args) 

    node = OccupancyGridPublisher() 

  

    try: 

        rclpy.spin(node) 

    except KeyboardInterrupt: 

        pass 

  

    node.destroy_node() 

    rclpy.shutdown() 

  

  

if __name__ == '__main__': 

    main() 