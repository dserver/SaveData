from pywinauto import application

def InitialRequest():
	info = {
		"parts" : None,
		"transactions" : []
	}
	datapage = application.Application()
	datapage.connect_(title_re="DataPage for Windows")
	datapage.DataPage.MenuSelect("Reports -> Spreadsheet Report...")
	datapage.connect_(title_re="Spreadsheet Report")
	info["parts"] = datapage.Spreadsheet.ComboBox1.ItemTexts()
	transactions_list = []
	parts_number_items = datapage.Spreadsheet.ComboBox1.ItemCount()
	for i in range(0,parts_number_items):
		datapage.Spreadsheet.ComboBox1.Select(i)
		transaction = datapage.Spreadsheet.ListBox3.ItemTexts()
		info["transactions"].append(transaction)
		
	datapage.Spreadsheet.Cancel.Click()
	return info
	
	

def SelectPartTransaction(part, transaction):
	datapage = application.Application()
	datapage.connect_(title_re="DataPage for Windows")
	datapage.DataPage.MenuSelect("Reports -> Spreadsheet Report")
	datapage.connect_(title_re="Spreadsheet Report")
	datapage.Spreadsheet.ComboBox1.Select(part)
	datapage.Spreadsheet.ListBox3.Select(transaction)
	datapage.Spreadsheet.ComboBox2.Select("MEAS_ORDER")
	datapage.Spreadsheet.Ok.Click()
	
def GetSaveFolders():
	datapage = application.Application()
	datapage.connect_(title_re="DataPage for Windows")
	datapage.DataPage.MenuSelect("File -> Save to File -> Save Current Report")
	datapage.connect_(title_re="Save As")
	print "Attempting to get folders...(datapage layer)"
	folders = datapage["Save As"].ListBox2.ItemTexts()
	datapage["Save As"].Cancel.Click()
	print "Got folders, returning to socket layer"
	return folders
	
def SaveAs(filename, folder):
	datapage = application.Application()
	datapage.connect_(title_re="DataPage for Windows")
	datapage.DataPage.MenuSelect("File -> Save to File -> Save Current Report")
	datapage.connect_(title_re="Save As")
	print filename
	print folder
	datapage["Save As"].editbox1.SetEditText(filename)
	datapage["Save As"].listbox2.Select(folder)
	datapage["Save As"].listbox2.DoubleClick(coords=(10,80))
	datapage["Save As"].Ok.Click()