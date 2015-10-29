#! /usr/bin/env python
from config_index import *
import rospy
import rosbag
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, String
import genpy



def store(dict, name_archive="test"):
	bag = rosbag.Bag(name_archive + ".bag", 'w')
	try:
		for key in dict.keys():
			topic = dict[key][topic_index]
			msg = dict[key][msg_index]
			rate = dict[key][rate_index]
			bag.write(topic,msg,rate)
	finally:
		bag.close()
ls=["/odom",Twist(),genpy.Time(1,0),Twist()]
ls2=["/odom",Twist(),genpy.Time(2,2),Twist()]
ls3=["/odom",Twist(),genpy.Time(3,1),Twist()]
store_dict=dict([("1",ls),("2",ls2),("3",ls3)])
store(store_dict, "test")