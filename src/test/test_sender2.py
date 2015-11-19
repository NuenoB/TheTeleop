#! /usr/bin/env python
import genpy
import rospy
from std_msgs.msg import String
import roslib
import roslib.message
import yaml

def sender1(msg, reciver, msg_type):
	#reciver -> String
	#msg -> obj
	#rospy.init_node('sender', anonymous=True)
	#rospy.loginfo("sender " + reciver)
	msg_class = roslib.message.get_message_class(msg_type)
	pub = rospy.Publisher(reciver, msg_class , queue_size=0)
	#rospy.loginfo(msg)
	# type-case using YAML
	#pub_args = []
	#msgg = var.split()
	aux_args = yaml.load(var)
	
	#try:
	#	for m in msgg:
	#		pub_args.append(yaml.load(m))
	#except Exception as e:
	#	print e
	#parser.error("Argument error: "+str(e))

	rate = rospy.Rate(10)
	msg = msg_class()
	now = rospy.get_rostime() 
	import std_msgs.msg
	keys = { 'now': now, 'auto': std_msgs.msg.Header(stamp=now) }
	genpy.message.fill_message_args(msg, aux_args, keys=keys)
	x=0
	while x<2 :
		pub.publish(msg)
		rate.sleep()
		x=x+1
	#rospy.loginfo("sended ")

var = """
linear:
  x: 1.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0
  """

rospy.init_node('The_Teleop')
#ls=["/odom",Twist(),genpy.Time(1,0),Twist]
sender1(var,"/odom", "geometry_msgs/Twist")

#from optparse import OptionParser
#parser = OptionParser(usage="[args...]", prog = "Algo")
#(options, msgg) = parser.parse_args(var)
#print msgg
	