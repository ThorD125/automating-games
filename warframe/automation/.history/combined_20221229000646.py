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


image = "___"


def needimage():
    # search = Search(image)
    # pos = search.imagesearch()
    # return pos[0] != -1 if image != '___' else True
    return Search(image).imagesearch()[0] != -1 if image != '___' else True


# needimage("onkonobg.png")


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
        b.start()
        mykeypressedboard.wait("9")
        print("Ended")
        global endthread
        endthread = True
        b.join()


frames = ["trinity", "harrow", "nekros"]


while True:
    # global image
    image = '___'
    frame = input("input")
    time.sleep(10)
    print("start")
    endthread = False
    looplogic()
    print("end")
