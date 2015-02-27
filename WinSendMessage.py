import win32gui, win32process, win32ui, win32api
import sys
import re
import ctypes


# Globals
found = False
_hwnd = None
_child_hwnd = None
_listbox1_hwnd = None
LB_SELECTSTRING = 396

def enum_window_callback(hwnd, extra):
    find_title = re.compile(re.escape(extra[0]))
    wintitle = win32gui.GetWindowText(hwnd)
    #print wintitle
    matches = re.findall(find_title, wintitle)
    if len(matches)>0:
        global found
        global _hwnd
        found = True
        _hwnd = hwnd
        
def enum_child_callback(hwnd, extra):
    find_title = re.compile(re.escape(extra[0]))
    wintitle = win32gui.GetWindowText(hwnd)
    winclass = win32gui.GetClassName(hwnd)
    wintext = win32gui.GetWindowText(hwnd)
    print "Title: " + wintitle + " Class: " + winclass + " Text: " + wintext
    if winclass == "ComboLBox":
        dlg_int = win32gui.GetDlgCtrlID(hwnd)
        print "Found ID"
        print dlg_int
        dlg_text = win32gui.GetDlgItemText(hwnd,dlg_int)
        print "Dlg_Int: " + dlg_int + " Dlg_Text: " + dlg_text
    matches = re.findall(find_title, wintitle)
    if len(matches)>0:
        global found
        global _child_hwnd
        found = True
        _child_hwnd = hwnd
        #print wintitle
        #return False # needed to stop enumerating through windows
    else:
        found = False

# for each window handle found, enum_window_callback is called
def find_window(title):
    win32gui.EnumWindows(enum_window_callback, (title,))

def find_child_window(threadId, child_title):
    win32gui.EnumThreadWindows(threadId, enum_child_callback, (child_title,))

find_window("Notepad++")
if not found:
    sys.exit(0)

# The thread returned is the same thread returned if you use _child_hwnd
(threadId, processId) = win32process.GetWindowThreadProcessId(_hwnd)
try:
    find_child_window(threadId, "Preferences")
except Exception as e:
    print e
    pass # upon returning false in the enum_child_callback and error will be raised

if not found:
    print "Couldn't find child window"
    sys.exit(0)

print "Found preferences window"


try:
    _listbox1_hwnd = win32gui.FindWindowEx(_hwnd, None, "ListBox1", None)
    if _listbox1_hwnd == 0:
        raise Exception("Listbox1 wasn't found!")
except Exception as e:
    print e
    sys.exit(0)

print "Found Listbox1"
text = "Print"
try:
    er = win32api.SendMessage(_listbox1_hwnd, 396,-1,r"Print")
    if er == 0:
        raise Exception("Text from listbox 1 was not selected")
except Exception as e:
    print e
    sys.exit(0)
print "Selected text item from listbox"
