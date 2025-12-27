cmake_minimum_required(VERSION 3.0.2)
project(bumperbot_examples)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  turtlesim
  tf2_ros
  geometry_msgs
  message_generation
)
catkin_python_setup()
add_service_files(
  FILES
  AddTwoInts.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

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
  nodes/tf_example_node.py
  nodes/simple_timer.py
  nodes/simple_service_server.py
  nodes/simple_service_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
