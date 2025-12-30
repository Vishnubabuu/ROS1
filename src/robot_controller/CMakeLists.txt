cmake_minimum_required(VERSION 3.0.2)
project(robot_controller)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  sensor_msgs
  nav_msgs
  tf2
  tf2_ros
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS 
  roscpp
  rospy 
  std_msgs
  geometry_msgs
  sensor_msgs
  nav_msgs
  tf2
  tf2_ros
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  nodes/simple_controller_node.py
  nodes/noisy_controller_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
