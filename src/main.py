#! /usr/bin/env python
from config_index import *
from writebag import store
from readbag import restore
from sender import sender
import roslib
import roslib.message
import rospy, tty, termios, sys, select
import yaml
import genpy

def newGetKey():
	settings = termios.tcgetattr(sys.stdin)
	tty.setraw(sys.stdin.fileno())
	#rlist, _, _ = select.select([sys.stdin], [], [], 5.0)#esperar
	#if rlist:
	key = sys.stdin.read(1)	
	#else:
	#	key = ''
	#finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

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
	mantener=1;
	while(mantener): 	
		print "input key"
		#getkey
		key = newGetKey()
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
			sender(msg, topic, msg_type) 
		elif key=="e":
			mantener=0
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
		dictio = borrar(dictio)
	elif(key=="a"):
		dictio = agregar(dictio)

	elif(key=="c"):
		print "change"
		dictio = modificar(dictio)
	print dictio
	return dictio


def agregar(dictio):
	key = getkey("a key pliss")
	topico = getLine("a topic pliss")
	line =""
	msg1 = getLine("a menssage pliss")
	while (msg1)!="":
		line +=str(msg1)
		msg1 = getLine()
	#msg = getLine("a menssage pliss")
	rate = getLine("a rate pliss")
	msg_type = getLine("the type of the menssage pliss")
	if dictio.has_key(key):
		print "tecla asociada a otro boto, para cambiar, seleccion change"
	else:
		msg_class = roslib.message.get_message_class(msg_type)
		msgx = msg_class()
		aux_args = yaml.load(line)
		print aux_args
		now = rospy.get_rostime()
		import std_msgs.msg
		keys = { 'now': now, 'auto': std_msgs.msg.Header(stamp=now) }
		genpy.message.fill_message_args(msgx, aux_args, keys=keys)
		newElement = [topico, msgx , rate ,msg_type]
		dictio[key] = newElement
		print "new command agregado"
	return dictio

def borrar(dictio):
	key = getkey("a key please")
	if (dictio.has_key(key)):
		del dictio[key]
		print "key deleted successfully"
	else:
		print "key undefined"
	return dictio

def modificar(dictio):
 	old_key = getkey("select old key")
 	if (dictio.has_key(old_key)):
 		new_key = getkey("select new key")
 		#look for
 		element = dictio[old_key]
		del dictio[old_key]
		dictio[new_key] =element
		print "key changed successfully"
	else:
		print "key undefined"
	return dictio

main()
