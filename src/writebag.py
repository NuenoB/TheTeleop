#! /usr/bin/env python
from config_index import *
import rospy
import rosbag
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, String
import genpy
from rqt_TheTeleop.msg import boton_data


def store(dict, name_archive="test"):
	bag = rosbag.Bag(name_archive + ".bag", 'w')
	try:
		t = 1
		for key in dict.keys():
			topic = dict[key][topic_index]
			msg = dict[key][msg_index]
			rate = dict[key][rate_index]
			strr = str(key)
			print key 
			print msg
			st= boton_data(strr,rate)
			#print strr
			#print st
			#print genpy.Time(t,0)
			#print genpy.Time(t,1) 
			bag.write(topic,msg,genpy.Time(t,0))
			bag.write("/test",st,genpy.Time(t,1))
			t = t+1
	finally:
		bag.close()

ls=["/odom",Twist(),genpy.Time(1,0),Twist()]
ls2=["/odom",Twist(),genpy.Time(2,2),Twist()]
ls3=["/odom",Twist(),genpy.Time(3,1),Twist()]
ls4=["/odom",Twist(),genpy.Time(3,1),Twist()]
ls5=["/odom",Twist(),genpy.Time(3,1),Twist()]
store_dict=dict([("1",ls),("2",ls2),("3",ls3),("4",ls4),("5",ls5)])
store(store_dict, "test")	