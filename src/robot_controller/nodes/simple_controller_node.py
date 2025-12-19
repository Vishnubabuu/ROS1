#!/usr/bin/env python3
import rospy
from robot_controller.simple_controller import simple_controller

if __name__ == '__main__':
    rospy.init_node('simple_controller', anonymous=True)

    # Read private parameters
    wheel_radius = rospy.get_param('~wheel_radius')
    wheel_separation = rospy.get_param('~wheel_separation')
    controller = simple_controller(wheel_radius, wheel_separation)
    rospy.spin()
