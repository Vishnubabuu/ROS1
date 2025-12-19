#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import numpy as np

class simple_controller(object):
    def __init__(self, wheel_radius, wheel_separation):
        rospy.loginfo("simple_controller initialized with wheel radius: %d and wheel separation: %d",
                      wheel_radius, wheel_separation)

        self.right_cmd_pub_ = rospy.Publisher('/wheel_right_controller/command', Float64, queue_size=10)
        self.left_cmd_pub_  = rospy.Publisher('/wheel_left_controller/command', Float64, queue_size=10)

        self.vel_sub_ = rospy.Subscriber('robot_controller/cmd_vel', Twist, self.velcallback)

        self.speed_conversion_ = np.array([
            [wheel_radius/2, wheel_radius/2],
            [wheel_radius/wheel_separation, -wheel_radius/wheel_separation]
        ])

        rospy.loginfo("Conversion matrix: %s", self.speed_conversion_)

    def velcallback(self, msg):
        robot_speed = np.array([[msg.linear.x], [msg.angular.z]])
        wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion_), robot_speed)

        right_speed = Float64(wheel_speed[0,0])
        left_speed  = Float64(wheel_speed[1,0])

        self.right_cmd_pub_.publish(right_speed)
        self.left_cmd_pub_.publish(left_speed)
