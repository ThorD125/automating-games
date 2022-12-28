import time
import pyautogui
import keyboard
import win32gui

warframeapp = "2623744"
# warframeapp = win32gui.FindWindow(None, "Notepad")

oldwindow = win32gui.GetForegroundWindow()

time.sleep(3)

print(oldwindow)
win32gui.SetForegroundWindow(warframeapp)

keyboard.press('a')
keyboard.release('a')

win32gui.SetForegroundWindow(oldwindow)

# def click():
#     pyautogui.press("NUM2")
#     click()


# click()
