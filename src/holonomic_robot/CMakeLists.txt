cmake_minimum_required(VERSION 3.5) 

project(holonomic_robot) 

 

find_package(ament_cmake REQUIRED) 

find_package(rclpy REQUIRED) 

find_package(nav2_simple_commander REQUIRED) 

find_package(geometry_msgs REQUIRED) 

 

install(DIRECTORY launch urdf config scripts 

  DESTINATION share/${PROJECT_NAME} 

) 
install(
  PROGRAMS scripts/navigate_robot.py  # Lista de scripts ejecutables
  DESTINATION lib/${PROJECT_NAME}
)


ament_package() 
message("Instalacion completa")