import pylewm.focus
import pyvda
from pylewm.commands import PyleCommand

@PyleCommand
def move_window_to_desktop_number(n):
    window = pylewm.focus.FocusWindow
    if(window):
        pyvda.MoveWindowToDesktopNumber(window.handle, n) 

@PyleCommand
def get_current_desktop_number():
    return pyvda.GetCurrentDesktopNumber() 

@PyleCommand
def get_window_desktop_number(window):
    return pyvda.GetWindowDesktopNumber(window.handle)

@PyleCommand
def get_desktop_count():
    return pyvda.GetDesktopCount()

@PyleCommand
def go_to_desktop_number(n=0):
    pyvda.GoToDesktopNumber(n)
