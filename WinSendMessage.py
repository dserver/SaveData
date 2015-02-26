import win32api, win32con, win32gui, win32ui, win32service, os, time

class Window:
    def __init__(self):
        self._hwnd = None
        self._text = None

def enum_window_callback(hwnd, extra):
    print win32gui.GetWindowText(hwnd)

def enum_windows():
    win32gui.EnumWindows(enum_window_callback, None)

def get_window_by_text(wintext):
    pass

enum_windows()

