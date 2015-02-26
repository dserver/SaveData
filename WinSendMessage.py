import win32gui, win32process
import sys
import re

class Window:
    def __init__(self):
        self._hwnd = None
        self._text = None


# Globals
found = False
_hwnd = None
_child_hwnd = None


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
    print wintitle
    matches = re.findall(find_title, wintitle)
    if len(matches)>0:
        global found
        global _child_hwnd
        found = True
        _child_hwnd = hwnd
        return False # needed to stop enumerating through windows
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


(threadId, processId) = win32process.GetWindowThreadProcessId(_hwnd)

find_child_window(threadId, "Preferences")

if not found:
    print "Couldn't find child window"
    sys.exit(0)

print "Found preferences window"
print _child_hwnd
