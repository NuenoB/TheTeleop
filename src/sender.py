#! /usr/bin/env python

import rospy
from std_msgs.msg import String
import roslib


def sender(msg,reciver, msg_type):
	#reciver -> String
	#msg -> obj
	#
	#rospy.init_node('sender', anonymous=True)
	#rospy.loginfo("sender " + reciver)
	msg_class = roslib.message.get_message_class(msg_type)
	pub = rospy.Publisher(reciver, msg_class , queue_size=0)
	#rospy.loginfo(msg)
	rate = rospy.Rate(10)
	x=0
	while x<2 :
		pub.publish(msg)
		rate.sleep()
		x=x+1
	#rospy.loginfo("sended ")
	rospy.spin()

