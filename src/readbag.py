
import rosbag
bag = rosbag.Bag('test.bag')
#saber los topicos
var = bag.get_type_and_topic_info()[1]
topics = bag.get_type_and_topic_info()[1].keys()
print bag.get_type_and_topic_info()
# saber los tipos
#types = []
#for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
#	types.append(bag.get_type_and_topic_info()[1].values()[i][0])

for topic, msg, t in bag.read_messages():
	print str(topic)
	print str(msg)
	print str(t)
	print str(var[topic][0])
bag.close()