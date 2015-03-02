import socket
import sys
from os import strerror as os_strerror
import cPickle as pickle

# A simple protocol for sending and receiving messages between the client_msg
# and the server

class SimpleProtocolException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

# Put a msg (as a string via pickle or literal)
# The function will send the message length and then
# the message. The server will do a recv_msg to get both values
def send_msg(msg, sock):
	try:
		msg_len = len(msg)
		msg_len = int_to_msg(msg_len)
		sock.sendall(msg_len)
		sock.sendall(msg)
	except socket.error as e:
		print e.value
		raise(SimpleProtocolException("send_msg encountered a socket error"))

# Receives an incoming message by listening first for
# the message size and then receiving the message. It
# returns the message string sent
def recv_msg(sock):
	try:
		mls = sock.recv(4)
		mli = msg_to_int(mls)
		msg = sock.recv(mli)
		return msg
	except socket.error as e:
		print e.value
		raise(SimpleProtocolException("recv_msg encountered a socket error"))

# When a message is sent over the wire, it will be a 4 byte
# ascii representation. This will change it to its integer representation
def msg_to_int(client_msg):
	try:
		return int(client_msg)
	except (RuntimeError, TypeError, NameError) as e:
		print e
		raise(SimpleProtocolException("msg_to_int encountered a fatal error"))
	
# When you want to send a message, pass the length of the string
# to this function and it will return a 4 byte ascii representation
# that can be sent over the wire
def int_to_msg(length):
	try:
		if length >= 10000:
			print "msg length is too long"
		str_length = str(length)
		msg = ""
		if (len(str_length) == 1):
			msg = "000" + str_length
		if (len(str_length) == 2):
			msg = "00" + str_length
		if (len(str_length) == 3):
			msg = "0" + str_length	
		if (len(str_length) == 4):
			msg = str_length
		return msg
	except (RuntimeError, TypeError, NameError) as e:
		print e.value
		raise(SimpleProtocolException("int_to_msg encountered a fatal error"))