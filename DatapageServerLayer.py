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
		datapage.Spreadsheet.ComboBox1.Select(0)
		transaction = datapage.Spreadsheet.ListBox3.ItemTexts()
		info["transactions"].append(transaction)
	return info
	
	

		