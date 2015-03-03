
from SimpleProtocol import send_msg, recv_msg, SimpleProtocolException
import socket
import cPickle as pickle
import time

class ClientSocket:
	def __init__(self):
		self.connection = ('abrune', 10004) # Connection to Datapage PC
		
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
		
	def send_parts_transactions(self, parts, transactions):
		try:
			data = {
				"part":parts,
				"transaction":transactions
			}
			
			pickled_data = pickle.dumps(data) # the data to be sent to the server is now pickled
			
		except (pickle.UnpicklingError, AttributeError, EOFError, IndexError, RuntimeError, TypeError) as e:
			print "Error in client socket sending parts/transactions"
			print e
			
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(self.connection)
		except socket.error as e:
			print "Error creating socket. ClientSocket.send_parts_transactions."
			print e
			
		try:
			send_msg("Part and Transaction", s)
			send_msg(pickled_data, s) # Bombs away!
		except SimpleProtocolException as e:
			print e
	
	def recv_save_folders(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#s.setdefaulttimeout(8)
			s.connect(self.connection)

		except socket.error as e:
			print "Error creating socket. ClientSocket.send_parts_transactions."
			print e
		
		try:
			send_msg("Recv Save Folders", s)
			folders_pickled = recv_msg(s)
			folders = pickle.loads(folders_pickled)
		except Exception as e:
			print e
		return folders
	
	def save_as(self, filename, folder):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(self.connection)
		except socket.error as e:
			print "Error creating socket. ClientSocket.send_parts_transactions."
			print e
		
		try:
			data = {
				"filename":filename,
				"folder":folder
			}
			
			data_pickled = pickle.dumps(data)
			
		except (pickle.UnpicklingError, AttributeError, EOFError, IndexError, RuntimeError, TypeError) as e:
			print e
		
		try:
			send_msg("Save As", s)
			send_msg(data_pickled, s)
		except SimpleProtocolException as e:
			print e
		
	def close_server(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(self.connection)
		send_msg("Exit", s)
