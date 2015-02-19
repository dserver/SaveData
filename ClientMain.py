from ClientGui import ClientGui
from ClientSocket import ClientSocket

class ClientMain:
	def __init__(self):
		self.gui = ClientGui()
		self.gui.set_connectbutton_command(self.get_parts_transactions)
		self.gui.start_tkinter_thread()
		
		self.socket_layer = ClientSocket()
		self.debug = True
		
	def get_parts_transactions(self):
		if (self.debug):
			self.gui.fill_parts_transactions(['part1', 'part2', 'part3'], ['t1', 't2'])
			return
		
		try:
			(parts, transactions) = self.socket_layer.initial_request()
		except Exception as e:
			print e.value
				return
		self.gui.fill_parts_transactions(parts, transactions)
	
	def send_parts_transactions(self):

main_program = ClientMain()