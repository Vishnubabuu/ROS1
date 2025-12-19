#!/usr/bin/env python3
import rospy
import math
from turtlesim.msg import Pose

class turtlesimkinematics(object):
    def __init__(self):
        self.turtle1_pose_sub= rospy.Subscriber('/turtle1/pose', Pose, self.turtle1_pose_callback)
        self.turtle2_pose_sub= rospy.Subscriber('/turtle2/pose', Pose, self.turtle2_pose_callback)
        
        self.last_turtle1_pose_= Pose()
        self.last_turtle2_pose_= Pose()
        
    def turtle1_pose_callback(self, pose):
        self.last_turtle1_pose_ = pose
        
    def turtle2_pose_callback(self, pose):
        self.last_turtle2_pose_ = pose
        
        Tx= self.last_turtle2_pose_.x - self.last_turtle1_pose_.x
        Ty= self.last_turtle2_pose_.y - self.last_turtle1_pose_.y
        
        theta_rad= self.last_turtle2_pose_.theta - self.last_turtle1_pose_.theta
        theta_deg= theta_rad * (180.0 / 3.141592653589793)
        
        
        rospy.loginfo("""................................
            Translation vector turtle1 -> turtle2\n
            Tx: %f\n
            Ty: %f\n
            Rotation Matrix turtle1 -> turtle2\n
            theta(rad): %f\n
            theta(deg): %f\n
            | R11   R12| : |%f   %f|\n
            | R21   R22| : |%f   %f|\n
            Transformation Matrix turtle1 -> turtle2\n
            | R11   R12   Tx| : |%f   %f   %f|\n
            | R21   R22   Ty| : |%f   %f   %f|\n
            | 0      0     1| : |0      0     1|\n
            .................................
            """, Tx, Ty, theta_rad, theta_deg, 
            math.cos(theta_rad), -math.sin(theta_rad),
            math.sin(theta_rad), math.cos(theta_deg),
            math.cos(theta_rad), -math.sin(theta_rad), Tx,
            math.sin(theta_rad), math.cos(theta_rad), Ty)
  
        