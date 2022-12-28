from cmd import PROMPT
from screen_search import *
from pynput.keyboard import Key, Controller
import time
import msvcrt
import time
import threading

import keyboard as mykeypressedboard

keyboard = Controller()


def clicking(key, castingdelay, castingtime, cooldown):
    time.sleep(castingdelay)
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(castingtime)
    time.sleep(cooldown)


global image

image = "___"


def needimage():
    if image != '___':
        return Search(image).imagesearch()[0] != -1
    else:
        return True


def mythread():
    print("inmythread")
    while needimage():
        if endthread or "nomatch" == clicklogic():
            break


frame = "trinity"


def clicklogic():
    global image
    match frame:
        case "trinity":
            clicking("2", 0, 0, 0.1)
        case "harrow":
            image = "harrow.png"
            clicking("4", 5, 7, 14)
        case "nekros":
            image = "___"
            clicking("2", 0, 0, 10)
        case _:
            image = "___"
            return "nomatch"


b = ""

endthread = False


def looplogic():
    print("inlooplogic")
    if frame in frames:
        global b
        b = threading.Thread(name='background', target=mythread)
        time.sleep(5)
        b.start()
        mykeypressedboard.wait("9")
        print("Ended")
        global endthread
        endthread = True
        b.join()
        time.sleep(5)
    else:
        print("frame not in frames")


frames = ["trinity", "harrow", "nekros"]


while True:
    image = '___'
    frame = input("input")
    print("start")
    endthread = False
    looplogic()
    print("end")
