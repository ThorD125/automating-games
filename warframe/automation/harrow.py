from screen_search import *
from pynput.keyboard import Key, Controller
import time
import msvcrt
import time
import threading

import keyboard as mykeypressedboard

keyboard = Controller()

time.sleep(10)

endthread = True


def clicking(key=1, castingdelay=0, castingtime=0, cooldown=0):
    time.sleep(castingdelay)
    keyboard.press(key)
    keyboard.release(key)
    print("delay for casting")
    time.sleep(castingtime)
    print("delay for cooldown")
    time.sleep(cooldown)


def mythread():
    search = Search("onkonobg.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        clicking("4", 5, 7, 14)
    else:
        print("else")
        time.sleep(1)
    if endthread:
        mythread()

    # if msvcrt.kbhit():
    #     if msvcrt.getch() == b'\x1b':
    #         break
b = threading.Thread(name='background', target=mythread)
# b = threading.Thread(target=mythread, args=(lambda: endthread,))

b.start()
mykeypressedboard.wait("9")
print("Ended")
endthread = False
b.join()
