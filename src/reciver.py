#! /usr/bin/env python

import rospy
from sender import *
from std_msgs.msg import String

def reciver(msg,reciver, msg_type):
	#reciver -> String
	#msg -> obj
	#rospy.loginfo("reciver " + reciver)
	rospy.Subscriber(reciver, msg_type, testeo)

def testeo(data):
	#rospy.loginfo("testeo " + str(data))
	if (str(data) == 'hi'):
		print "its work"
	else:
		print "error error"


def main():
	rospy.init_node('testeo')
	reciver('hi','test_topic',String)
	sender('hi','test_topic',String)
	rospy.spin()

main()