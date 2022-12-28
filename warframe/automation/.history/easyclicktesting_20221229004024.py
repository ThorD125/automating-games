import time
import pyautogui
import keyboard
import win32gui

notepad_handle = win32gui.FindWindow(None, "Unitled - Notepad")

time.sleep(3)
window = win32gui.GetForegroundWindow()

print(window)
# Set the focus to the Notepad window
win32gui.SetForegroundWindow(notepad_handle)

# Send the key press event to the Notepad window
keyboard.press('a')
keyboard.release('a')


pyautogui.press("{NUMPAD2}")
# def click():
#     pyautogui.press("NUM2")
#     click()


# click()
