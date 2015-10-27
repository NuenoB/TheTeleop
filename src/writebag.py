import rospy
import rosbag
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32, String
import genpy



def store(msg ,msg_type, topic, rate, name_archive):
	bag = rosbag.Bag(name_archive + ".bag", 'w')
	try:
		bag.write(topic,msg,rate)
	finally:
		bag.close()

store(Twist(),"","/odom",genpy.Time.from_sec(55.0),"test")