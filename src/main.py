#! /usr/bin/env python
from writebag import *
from readbag import *
from sender import *
import rospy
def getkey():
	return input()

def main():
	rospy.init_node('The_Teleop')
	print "welcome to teleop"
	robot_name = str(input("set robot"))
	robot_setting = restore(robot_name) 
	reconfig_key="r"
	store_key ="s"
	print robot_setting
	print 
	while(1): 	
		print "input key"
		#getkey
		key=getkey()
		#if confign
		if key==reconfig_key:
			#call config
			print "reconfigurar"
			#reconfigurar()
		elif key ==store_key:
			name_bag=input("name the bag")
			print "saving the private bag"
			store(robot_setting,name_bag)
			print "saved"
		elif key in robot_setting:
			print "sending menssage"
			#if lookup is 
			#send()
			#mensaje = lookup(key)
			#sender(mensaje[0],mensaje[1],mensaje[2])
		else:
			#if lookup fails
			#insult the user
			print "invalid key"


main()