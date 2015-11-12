#! /usr/bin/env python
import genpy
import rospy
from std_msgs.msg import String
import roslib
import roslib.message

#rospy.loginfo("sender " + reciver)
inas = input("get a type")
msg_class = roslib.message.get_message_class("std_msgs/String")
#msg_class = roslib.message.get_message_class(topic_type)


print msg_class