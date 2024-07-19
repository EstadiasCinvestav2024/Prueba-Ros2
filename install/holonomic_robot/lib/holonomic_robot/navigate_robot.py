from nav2_simple_commander.robot_navigator import BasicNavigator, NavigationResult 

import rclpy 

from geometry_msgs.msg import PoseStamped 

from rclpy.duration import Duration 

 

def main(): 

    rclpy.init() 

 

    navigator = BasicNavigator() 

 

    # Wait for Nav2 to become active 

    navigator.waitUntilNav2Active() 

 

    # Initial pose can be set if needed 

    # initial_pose = PoseStamped() 

    # initial_pose.header.frame_id = 'map' 

    # initial_pose.header.stamp = navigator.get_clock().now().to_msg() 

    # initial_pose.pose.position.x = 0.0 

    # initial_pose.pose.position.y = 0.0 

    # initial_pose.pose.orientation.z = 0.0 

    # initial_pose.pose.orientation.w = 1.0 

    # navigator.setInitialPose(initial_pose) 

 

    goal_pose = PoseStamped() 

    goal_pose.header.frame_id = 'map' 

    goal_pose.header.stamp = navigator.get_clock().now().to_msg() 

    goal_pose.pose.position.x = 2.0 

    goal_pose.pose.position.y = 2.0 

    goal_pose.pose.orientation.w = 1.0 

 

    navigator.goToPose(goal_pose) 

 

    while not navigator.isTaskComplete(): 

        feedback = navigator.getFeedback() 

        if feedback and feedback.navigation_time > Duration(seconds=600): 

            navigator.cancelTask() 

            break 

 

    result = navigator.getResult() 

    if result == NavigationResult.SUCCEEDED: 

        print("Goal reached!") 

    else: 

        print("Failed to reach the goal.") 

 

    rclpy.shutdown() 

 

if __name__ == '__main__': 

    main() 