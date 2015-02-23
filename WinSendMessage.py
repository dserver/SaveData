import win32api, win32con, win32gui, win32ui, win32service, os, time



def f_click(pycwnd):
        x=300
        y=300
        lParam = y <<15 | x
        pycwnd.SendMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam);
        pycwnd.SendMessage(win32con.WM_LBUTTONUP, 0, lParam);

def get_whndl(wintext):
        whndl = win32gui.FindWindowEx(0, 0, None, wintext)
        return whndl

def make_pycwnd(hwnd):       
        PyCWnd = win32ui.CreateWindowFromHandle(hwnd)
        return PyCWnd

def send_input_hax(pycwnd, msg):
    f_click(pycwnd)
    for c in msg:
        if c == "\n":
            pycwnd.SendMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
            pycwnd.SendMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
        else:
            pycwnd.SendMessage(win32con.WM_CHAR, ord(c), 0)
    pycwnd.UpdateWindow()

def fwindow(classname, winname):
	return win32gui.FindWindow(None,winname)
whndl = fwindow(None, "PC-DMIS")
print whndl
