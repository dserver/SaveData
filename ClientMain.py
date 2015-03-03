
# This is the equivalent of the main() function in C++. This is the entry point
# to the client side application. All Gui related events are handled through the
# ClientGui class, and all communication to the datapage computer is handled 
# through the ClientSocket class, which I call the 'socket layer'. 

# The logic of the program is defined through this class. The program has one single
# objective: to save data from datapage. I've broken this into two objectives.
# When you open datapage after a part is done you click the "Spreadsheet Report" icon,
# then you click the part program you ran, the transaction, set the variables to measure order,
# and then click "Ok". This is the first objective and its code is started via the
# 'get_parts_transactions()' function in this class.
# The second objective is what you do after you click "Ok" in the spreadsheet report
# window. That is, you click File->Save to File, which then brings up another screen
# where you give the file a name and select where to save it. 

from ClientGui import ClientGui
from ClientSocket import ClientSocket
import time
class ClientMain:
	def __init__(self):
		self.gui = ClientGui()
		self.gui.set_connectbutton_command(self.get_parts_transactions)
		self.gui.set_sendbutton_command(self.send_parts_transactions)
		#self.gui.set_sendbutton_command(self.closeserver)
		self.gui.set_savebutton_command(self.save_as)
		self.gui.set_closebutton_command(self.closeserver)
		self.gui.start_tkinter_thread()
		
		self.socket_layer = ClientSocket()
		self.debug = False
	
	# Handles all the logic for receiving initial parts and transactions lists
	def get_parts_transactions(self):
		if (self.debug):
			self.gui.fill_parts_transactions(['part1', 'part2', 'part3'], ['t1', 't2'])
			return
		
		try:
			info = self.socket_layer.initial_request()
		except Exception as e:
			print e
			return
		self.gui.fill_parts_transactions(info["parts"], info["transactions"])
		
	# Handles sending users selection on which part and transaction to save
	def send_parts_transactions(self):
		try:
			(part_selection, transaction_selection) = self.gui.get_parts_transactions()
			self.gui.remove_transactions_screen()
			self.gui.draw_save_as_screen()
			self.socket_layer.send_parts_transactions(part_selection, transaction_selection)
			time.sleep(1)
			folders = False
			while not folders:
				folders = self.socket_layer.recv_save_folders()
			self.gui.populate_folders(folders)
		except Exception as e:
			print "ClientMain.send_parts_transactions"
			print e
			
	def save_as(self):
		(filename, folder) = self.gui.get_save_as_data()
		self.socket_layer.save_as(filename, folder)
		
	def closeserver(self):
		self.socket_layer.close_server()
	
main_program = ClientMain()
