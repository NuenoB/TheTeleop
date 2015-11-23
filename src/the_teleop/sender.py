#! /usr/bin/env python
import genpy
import rospy
from std_msgs.msg import String
import roslib
import roslib.message

def sender(msg,reciver, msg_type):
	#reciver -> String
	#msg -> obj
	#rospy.loginfo("sender " + reciver)

	msg_class = roslib.message.get_message_class(msg_type)
	pub = rospy.Publisher(reciver, msg_class , queue_size=0)
	#rospy.loginfo(msg)
	rate = rospy.Rate(10)

	x=1
	while x<2 :
		pub.publish(msg)
		rate.sleep()
		x=x+1
	#rospy.loginfo("sended ")
	#rospy.spin()

def sender1(msg, reciver, msg_type):
	#reciver -> String
	#msg -> obj
	#rospy.init_node('sender', anonymous=True)
	#rospy.loginfo("sender " + reciver)
	msg_class = roslib.message.get_message_class(msg_type)
	pub = rospy.Publisher(reciver, msg_class , queue_size=0)
	#rospy.loginfo(msg)
	# type-case using YAML
	try:
		pub_args = []
		for m in msg:
			pub_args.append(yaml.load(m))
			
	except Exception as e:
		parser.error("Argument error: "+str(e))
	rate = rospy.Rate(10)
	msg = msg_class()
	now = rospy.get_rostime() 
	import std_msgs.msg
	keys = { 'now': now, 'auto': std_msgs.msg.Header(stamp=now) }
	genpy.message.fill_message_args(msg, pub_args, keys=keys)
	x=0
	while x<2 :
		pub.publish(msg)
		rate.sleep()
		x=x+1
	#rospy.loginfo("sended ")
	rospy.spin()