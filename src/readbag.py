
import rosbag

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
	#print bag.get_message_count();
	while True:
		try:
			temp = trios.next()
		except Exception, e:
			break
		
		topic = temp[topic_index]
		print topic 
		msg = temp[msg_index]
		print msg 
		temp = trios.next()
		key = temp[msg_index].data.key
        lmsg[key]=[topic,msg,t,var[topic][0]]
	bag.close()

	return lmsg

print restore()