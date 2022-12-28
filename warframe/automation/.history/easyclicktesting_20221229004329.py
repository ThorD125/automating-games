import time
import pyautogui
import keyboard
import win32gui

notepad_handle = win32gui.FindWindow(None, "Notepad")
warframeapp = "2623744"
warframeapp = "2623744"

oldwindow = win32gui.GetForegroundWindow()

time.sleep(3)
window = win32gui.GetForegroundWindow()

print(oldwindow)
# Set the focus to the Notepad window
win32gui.SetForegroundWindow(warframeapp)

# Send the key press event to the Notepad window
keyboard.press('a')
keyboard.release('a')

win32gui.SetForegroundWindow(oldwindow)

pyautogui.press("{NUMPAD2}")
# def click():
#     pyautogui.press("NUM2")
#     click()


# click()
