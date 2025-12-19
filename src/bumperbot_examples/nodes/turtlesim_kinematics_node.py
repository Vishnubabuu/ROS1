#!/usr/bin/env pytho3
import rospy
from bumperbot_examples.turtlesim_kinematics import turtlesimkinematics  


if __name__ == '__main__':
    rospy.init_node('turtlesim_kinematics_node', anonymous=True)
    tk= turtlesimkinematics()
    rospy.spin()