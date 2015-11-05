#! /usr/bin/env python
from config_index import *
from writebag import *
from readbag import *
from sender import *
import rospy
def getkey():
	return input()

def main():
	rospy.init_node('The_Teleop')
	print "welcome to teleop"
	#robot_name = str(input("set robot"))
	robot_name ="test"
	robot_setting = restore(robot_name) 
	reconfig_key="r"
	store_key ="s"
	print robot_setting
	print 
	while(1): 	
		print "input key"
		#getkey
		key=getkey()
		if key==reconfig_key:
			#call config
			reconfig()
		elif key ==store_key:
			name_bag=input("name the bag")
			print "saving the private bag"
			store(robot_setting,name_bag)
			print "saved"
		elif key in robot_setting:
			print "sending menssage"
			val = lookup(robot_setting,key)
			topic = val[topic_index]
			msg = val[msg_index]
			msg_type = val[type_index]
			print msg_type
			sender(msg, topic, msg_type) 
		else:
			#if lookup fails
			#insult the user
			print "invalid key"

def lookup(dictio,key):
	val=dictio[key]
	return val

def reconfig():
	if (borrar):
	elif(agregar):
	elif(modificar):
	newkey = getkey()

main()