from SimpleProtocol import send_msg, recv_msg, SimpleProtocolException
import DatapageServerLayer

class ServerSocket:
	def __init__(self):
		self.connection = ('abrune', 10001) 
		
	# Start the socket received loop
	def start_socket_recv_loop(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(self.connection)
		s.listen(1)
		
		while True:
			(shared_socket, address) = s.accept()
			
			command = recv_msg(shared_socket)
			
			if (command == "Init"):
				info = DatapageServerLayer.InitialRequest()
				send_msg(pickle.dumps(info), shared_socket)
		
		s.close()
		
		
