cmake_minimum_required(VERSION 3.0.2)
project(bumperbot_examples)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  turtlesim
  tf2_ros
  geometry_msgs
)
catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS turtlesim
  tf2_ros
  geometry_msgs
)


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)
catkin_install_python(PROGRAMS
  nodes/simple_publisher.py
  nodes/simple_subscriber.py
  nodes/turtlesim_kinematics_node.py
  nodes/tf_example.py
  nodes/simple_timer.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
