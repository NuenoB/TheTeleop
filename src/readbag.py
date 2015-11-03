
import rospy
import rosbag
from rqt_TheTeleop.msg import boton_data

# saber los tipos
#types = []
#for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
#	types.append(bag.get_type_and_topic_info()[1].values()[i][0])

topic_index=0
msg_index=1
rate_index=2
type_index=4


def restore(name_bag = "test"):
	bag = rosbag.Bag(name_bag + ".bag")
	var = bag.get_type_and_topic_info()[1]
	#topics = bag.get_type_and_topic_info()[1].keys()
	#print bag.get_type_and_topic_info()
	lmsg = dict()
	trios  = bag.read_messages()
	rospy.loginfo(bag.get_message_count())
	#for topic, msg, t in bag.read_messages():
	#	print msg
	while True:
		try:
			temp = trios.next()
			topic = temp[topic_index]
			msg = temp[msg_index]
			#print topic 
			#print msg 
			temp = trios.next()
			key = temp[msg_index].key1
			#print "key" + key
			t = temp[msg_index].time
			lmsg[key]=[topic,msg,t,var[topic][0]]
			#print len(lmsg)
		except Exception, e:
			rospy.loginfo("end of restore")
			break


	bag.close()
	print len(lmsg)
	return lmsg
