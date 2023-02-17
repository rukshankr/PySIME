import win32gui
import win32con

class MyIME:
    def __init__(self):
        # Create an IME context
        self.hIMC = win32gui.ImmCreateContext()
        # Set the IME's input mode to Hiragana
        self.set_input_mode(win32con.IMM_INPUTMODE_HIRAGANA)

    def handle_key_event(self, hwnd, msg, wparam, lparam):
        # Handle input events
        if msg == win32con.WM_CHAR:
            char = chr(wparam)
            # Process the input character
            print("Input character:", char)

    def set_input_mode(self, mode):
        # Set the IME's input mode
        win32gui.ImmSetConversionStatus(self.hIMC, mode, 0)

    def activate(self, hwnd):
        # Activate the IME
        win32gui.ImmAssociateContext(hwnd, self.hIMC)

    def deactivate(self, hwnd):
        # Deactivate the IME
        win32gui.ImmAssociateContext(hwnd, None)



# Create a window
hwnd = win32gui.CreateWindowEx(
    0, "Edit", "My Window", win32con.WS_OVERLAPPEDWINDOW,
    100, 100, 400, 400, 0, 0, 0, None)

# Create an instance of the MyIME class
ime = MyIME()

# Bind the IME to the window
win32gui.SetWindowLong(hwnd, win32con.GWL_IMECALLBACK, ime.handle_key_event)
ime.activate(hwnd)

# Show the window
win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

# Enter the event loop
win32gui.PumpMessages()
