import time
import pyautogui
import keyboard
import pywin32_system32

notepad_handle = pywin32_system32.FindWindow(None, "Notepad")

# Set the focus to the Notepad window
pywin32_system32.SetForegroundWindow(notepad_handle)

# Send the key press event to the Notepad window
keyboard.press('a')
keyboard.release('a')

time.sleep(3)


pyautogui.press("{NUMPAD2}")
# def click():
#     pyautogui.press("NUM2")
#     click()


# click()
