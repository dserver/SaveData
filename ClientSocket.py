
from SimpleProtocol import send_msg, recv_msg, SimpleProtocolException

class ClientSocket:
	def __init__(self):
		self.connection = ('abrune', 10001) # Connection to Datapage PC
		
	# Receives the parts and transactions data from Datapage
	def initial_request(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(self.connection)
		except socket.error as e:
			print e.value
			return
			
		try:
			send_msg("Init")
			
			# The server will send lists of lines that are in the parts box
			# and the transactions box
			parts_pickled = recv_msg(s)
			transactions_pickled = recv_msg(s)
		except SimpleProtocolException as e:
			print e.value
			return
			
		try:
			parts = pickle.loads(parts_pickled)
			transactions = pickle.loads(transactions_pickled)
		except (pickle.UnpicklingError, AttributeError, EOFError, IndexError, RuntimeError, TypeError) as e:
			print e.value
			return
		
		return (parts, transactions)