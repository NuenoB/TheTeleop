#! /usr/bin/env python
import genpy
import rospy
from std_msgs.msg import String
import roslib

#rospy.loginfo("sender " + reciver)
msg_class = roslib.message.get_message_class("std_msgs/Header")
print msg_class