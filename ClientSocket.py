
from SimpleProtocol import send_msg, recv_msg, SimpleProtocolException
import socket
import cPickle as pickle
class ClientSocket:
	def __init__(self):
		self.connection = ('abrune', 10002) # Connection to Datapage PC
		
	# Receives the parts and transactions data from Datapage
	def initial_request(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(self.connection)
		except socket.error as e:
			print e.value
			return
			
		try:
			send_msg("Init", s)
			
			# The server will send lists of lines that are in the parts box
			# and the transactions box
			info_pickled = recv_msg(s)
		except SimpleProtocolException as e:
			print e.value
			return
			
		try:
			info = pickle.loads(info_pickled)
		except (pickle.UnpicklingError, AttributeError, EOFError, IndexError, RuntimeError, TypeError) as e:
			print e.value
			return
		
		return info
	def close_server(self):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(self.connection)
		send_msg("Exit", s)
