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
	folders = datapage.DataPage["Save As"].ListBox2.GetTexts()
	datapage.DataPage["Save As"].Cancel.Click()
	return folders
	
def SaveAs(filename, folder):
	datapage = application.Application()
	datapage.connect_(title_re="DataPage for Windows")
	datapage.DataPage.MenuSelect("File -> Save to File -> Save Current Report")
	datapage.DataPage["Save As"].EditBox1.SetEditText(filename)
	datapage.DataPage["Save As"].ListBox2.Select(folder)
	datapage.DataPage["Save As"].Ok.Click()