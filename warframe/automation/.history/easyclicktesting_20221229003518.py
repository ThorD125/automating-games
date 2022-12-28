import time
import pyautogui
import keyboard
import win32gui


# Set the focus to the Notepad window
win32gui.SetForegroundWindow(win32gui.FindWindow("Notepad"))

# Send the key press event to the Notepad window
keyboard.press('a')
keyboard.release('a')

time.sleep(3)


pyautogui.press("{NUMPAD2}")
# def click():
#     pyautogui.press("NUM2")
#     click()


# click()
