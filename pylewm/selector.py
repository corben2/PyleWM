import win32gui
import fnmatch

def matches(hwnd, sel):
    if isinstance(sel, list) or isinstance(sel, tuple):
        for s in sel:
            if matches(hwnd, s):
                return True
        return False
    elif isinstance(sel, dict):
        if "class" in sel:
            cls = win32gui.GetClassName(hwnd)
            if not fnmatch.fnmatch(cls.lower(), sel["class"].lower()):
                return False
        if "title" in sel:
            title = win32gui.GetWindowText(hwnd)
            if not fnmatch.fnmatch(title.lower(), sel["title"].lower()):
                return False
        return True
    return None