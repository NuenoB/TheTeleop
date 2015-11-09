#! /usr/bin/env python
from config_index import *
from writebag import store
from readbag import restore
from sender import sender
import rospy

def getkey(arg =""):
	return input(arg)

def getLine(arg =""):
	return input(arg)


def main():
	rospy.init_node('The_Teleop')
	print "welcome to teleop"
	#robot_name = str(input("set robot"))
	robot_name ="test"
	robot_setting = restore(robot_name) 
	reconfig_key="r"
	store_key ="s"
	print robot_setting
	while(1): 	
		print "input key"
		#getkey
		key=getkey()
		if key==reconfig_key:
			#call config
			robot_setting = reconfig(robot_setting)
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

def reconfig(dictio):
	print dictio
	key = getkey("choose a option: a -> addCommand, c -> changeCommand, d->deleteComannd")
	if (key=="d"):
		print "delete"
		#borrar(dictio,key)
	elif(key=="a"):
		dictio = agregar(dictio)

	elif(key=="c"):
		print "change"
		#modificar(dictio,key)
	print dictio
	return dictio


def agregar(dictio):
	key = getkey("a key pliss")
	topico = getLine("a topic pliss")
	msg = getLine("a menssage pliss")
	rate = getLine("a rate pliss")
	msg_type = getLine("the type of the menssage pliss")
	if dictio.has_key('x'):
		print "tecla asociada a otro boto, para cambiar, seleccion change"
	else:
		newElement = [topico, msg , rate ,msg_type]
		dictio[key] = newElement 
		print "new command agregado"
	return dictio

#si el key no esta en el dicionario
main()