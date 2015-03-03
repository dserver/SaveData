from SimpleProtocol import send_msg, recv_msg, SimpleProtocolException
import DatapageServerLayer
import socket
import cPickle as pickle

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
			elif (command == "Part and Transaction"):
				# Grab the part and transaction to select
				print "Received Part/Transaction request..."
				data = recv_msg(shared_socket)
				print "Received data..."
				data = pickle.loads(data)
				print "Unpickled data! Sending to Datapage layer..."
				
				DatapageServerLayer.SelectPartTransaction(data["part"], data["transaction"])
				print "Selected the part and transaction..."
				
			elif (command == "Recv Save Folders"):
				folders = DatapageServerLayer.GetSaveFolders()
				send_msg(pickle.dumps(folders), shared_socket)
				print "Sent folders"
			elif (command == "Save As"):
				data_pickled = recv_msg(shared_socket) # recv the filename to save as and folder to save in
				data = pickle.loads(data_pickled)
				DatapageServerLayer.SaveAs(data["filename"], data["folder"])
				
			elif (command == "Exit"):
				break
			else:
				pass
		
		s.close()
		
		
s = ServerSocket()
s.start_socket_recv_loop()