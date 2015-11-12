#! /usr/bin/env python
from config_index import *
import rospy
import rosbag
import rospy.client
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, String
import genpy
from rqt_TheTeleop.msg import boton_data
from writebag import *
from readbag import *
import roslib


ls=["/odom",Twist(),genpy.Time(1,0),Twist]
store_dict=dict([("1",ls)])
store(store_dict, "test")

store_dict2=restore()

if(store_dict["1"][type_index]==store_dict2["1"][type_index]):
	print "wiii"
else :
	print "buuu"
	print rospy.get_published_topics()
	print store_dict["1"][type_index]
	print store_dict2["1"][type_index]
	print roslib.message.get_message_class(store_dict2["1"][type_index])