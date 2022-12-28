from screen_search import *
from pynput.keyboard import Key, Controller
import time
import msvcrt
import time
import threading

import keyboard as mykeypressedboard


def clicking(key=1, castingdelay=0, castingtime=0, cooldown=0):
    time.sleep(castingdelay)
    keyboard.press(key)
    keyboard.release(key)
    print("delay for casting")
    time.sleep(castingtime)
    print("delay for cooldown")
    time.sleep(cooldown)


def mythread():
    while True:
        clicking("2", 0, 0, 0.1)

        if endthread:
            break


keyboard = Controller()
key = "2"

time.sleep(10)

endthread = False
search = Search("exit.png")


b = threading.Thread(name='background', target=mythread)

b.start()
mykeypressedboard.wait("9")
print("Ended")
endthread = True
b.join()
