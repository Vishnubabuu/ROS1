#!/usr/bin/env python3
import rospy

def timerCallback(event=None):
    rospy.loginfo("Timer triggered at %s", event.current_real)

if __name__=="__main__":
    rospy.init_node('simple_timer_py',anonymous=True)
    timer_duration = rospy.Duration(1) # 1 second
    rospy.Timer(timer_duration, timerCallback)
    rospy.spin()
