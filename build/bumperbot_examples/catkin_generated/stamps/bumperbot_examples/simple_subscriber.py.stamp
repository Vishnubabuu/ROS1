#!usr/bin/env python3
import rospy
from std_msgs.msg import String

def msgcallback(msg):
    rospy.loginfo('new message recieved %s',msg.data)

if __name__=="__main__":
    rospy.init_node('bot_publisher',anonymous=True)
    rospy.Subscriber("chatter",String,msgcallback)
    
    rospy.spin()