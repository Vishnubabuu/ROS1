cmake_minimum_required(VERSION 3.0.2)
project(robot_localization)

find_package(catkin REQUIRED COMPONENTS
  rospy
  nav_msgs
  sensor_msgs
)

catkin_package()

###################################
# Python setup
###################################
catkin_install_python(
  PROGRAMS
    nodes/kalman_filter_node.py
    nodes/imu_republisher_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)