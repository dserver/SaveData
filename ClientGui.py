import threading
from Tkinter import *
import Tkinter

class ClientGui:
	def __init__(self):
		self.top = Tkinter.Tk() # Tkinter top window object
		self.screen_state = "transactions"
		
		##### PARTS AND TRANSACTIONS WIDGETS #########
		self.PartsListBox = Listbox(self.top, exportselection=0, width=60)
		self.PartsListBox.bind('<<ListboxSelect', self.parts_click)
		self.parts_contents = None # Initial request
		
		self.TransactionsListBox = Listbox(self.top, exportselection=0, width=60)
		self.transactions_contents = None  # Initial request
		
		self.ConnectButton = Button(self.top, text="Connect", width=25) # Calls initial request
		self.SendButton = Button(self.top, text="Send", width=25)
		
		##### SAVE AND CANCEL WIDGETS #####
		self.FolderListBox = Listbox(self.top, exportselection=0, width=30)
		self.FileNameEntry = Entry(self.top)
		self.FileNameEntry.insert(0, ".xls")
		self.SaveButton = Button(self.top, text="Save")
		self.CancelButton = Button(self.top, text="Cancel", command=self.draw_transactions_screen)
		self.FolderLabel = Label(self.top, text="Folder to save in")
		self.FileNameLabel = Label(self.top, text="Save as")
		
		self.draw_transactions_screen()
		
	def draw_save_as_screen(self):
		self.remove_transactions_screen()
		self.FolderListBox.grid(row=1, column=1)
		self.FileNameEntry.grid(row=2, column=1)
		self.SaveButton.grid(row=0, column=0)
		self.CancelButton.grid(row=0, column=1)
		self.FolderLabel.grid(row=1, column=0)
		self.FileNameLabel.grid(row=2, column=0)
	
	def remove_save_screen(self):
		self.FolderListBox.grid_remove()
		self.FileNameEntry.grid_remove()
		self.SaveButton.grid_remove()
		self.CancelButton.grid_remove()
		self.FolderLabel.grid_remove()
		self.FileNameLabel.grid_remove()
		
	def draw_transactions_screen(self):
		if (self.screen_state != "transactions"):
			self.remove_save_screen()
		
		# GRID DATA
		self.PartsListBox.grid(row=3, column=0)
		self.TransactionsListBox.grid(row=3,column=2)
		self.ConnectButton.grid(row=0, column=0)
		self.SendButton.grid(row=0, column=2)
		self.PartsLabel = Label(self.top, text="Parts").grid(row=1, column=0)
		self.TransactionsLabel = Label(self.top, text="Transactions").grid(row=1, column=2)
		
	def remove_transactions_screen(self):
		self.PartsListBox.grid_remove()
		self.TransactionsListBox.grid_remove()
		self.ConnectButton.grid_remove()
		self.SendButton.grid_remove()
		self.PartsLabel.grid_remove()
		self.TransactionsLabel.grid_remove()

	def fill_parts_transactions(self, parts, transactions):
		self.parts_contents = parts
		# fill parts box
		for i in range(len(parts)):
			self.PartsListBox.insert(i+1, parts[i])
	
	def set_connectbutton_command(self, func):
		self.ConnectButton.configure(command=func)
		
	def set_sendbutton_command(self, func):
		self.SendButton.configure(command=func)
		
	def set_savebutton_command(self, func):
		self.SaveButton.configure(command=func)
		
	def start_tkinter_thread(self):
		tkinter_thread = threading.Thread(target=self.top.mainloop)
		tkinter_thread.start()

	def parts_click(self):
		current = self.PartsListBox.curselection()
		for i in range(len(self.parts_contents)):
			if self.parts_contents[i] == current:
				break
		
		# i now holds the part index corresponds to the transaction
		# delete all previous transactions in the box
		self.TransactionsListBox.delete(0, self.TransactionsListBox.size())
		
		# add transactions for selected part
		for x in range(len(self.transactions_contents[i])):
			self.TransactionsListBox.insert(x+1, self.transactions_contents[i][x])
		
		
if __name__ == "__main__":
	g = ClientGui()
	g.start_tkinter_thread()
	g.SendButton.configure(command=g.draw_save_as_screen)
		