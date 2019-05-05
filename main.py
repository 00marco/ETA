import RPi.GPIO as GPIO
import time
import sys
from debouncer import *
#from test1 import *
#from test.test2 import *
import caption
#import webcam.py
import threading

sys.path.append('/home/pi/Desktop/ETA/pydnet-master/pydnet-master/') 
#add pydnet folder to sys.path so that we can import pydnet files directly
sys.path.append('/home/pi/Desktop/ETA/test/')
#test path

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#test1()
#test2i()

#Important pins (Broadcomm notation)
trigger_get_caption = 15
trigger_toggle_depth = 4

trigger_volume_up = 14
trigger_volume_down = 27

trigger_shutdown = 18
trigger_restart = 17

def get_caption(pin):
    start = time.time()
    print("image caption")
    print(caption.get_captions())
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
def toggle_depth(pin):
    start = time.time()
    print("toggle depth")
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
def volume_up(pin):
    start = time.time()
    print("volume up")
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
def volume_down(pin):
    start = time.time()
    #something
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
def shutdown(pin):
    start = time.time()
    #something
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
def restart(pin):
    start = time.time()
    #something
    end = time.time()
    print("{0} seconds elapsed".format(end - start))



GPIO.setup([trigger_get_caption, trigger_toggle_depth, trigger_volume_up, trigger_volume_down, trigger_shutdown, trigger_restart], GPIO.IN, pull_up_down=GPIO.PUD_UP)

cb1 = ButtonHandler(trigger_get_caption, get_caption, edge='falling', bouncetime=100)
cb1.start()

cb2 = ButtonHandler(trigger_toggle_depth, toggle_depth, edge='falling', bouncetime=100)
cb2.start()

cb3 = ButtonHandler(trigger_volume_up, volume_up, edge='falling', bouncetime=100)
cb3.start()

cb4 = ButtonHandler(trigger_volume_down, volume_down, edge='falling', bouncetime=100)
cb4.start()

cb5 = ButtonHandler(trigger_shutdown, shutdown, edge='falling', bouncetime=100)
cb5.start()

cb6 = ButtonHandler(trigger_restart, restart, edge='falling', bouncetime=100)
cb6.start()

GPIO.add_event_detect(trigger_get_caption, GPIO.FALLING, get_caption)
GPIO.add_event_detect(trigger_toggle_depth, GPIO.FALLING, toggle_depth)
GPIO.add_event_detect(trigger_volume_up, GPIO.FALLING, volume_up)
GPIO.add_event_detect(trigger_volume_down, GPIO.FALLING, callback=cb4)
GPIO.add_event_detect(trigger_shutdown, GPIO.FALLING, callback=cb5)
GPIO.add_event_detect(trigger_restart, GPIO.FALLING, callback=cb6)

while True:
    time.sleep(1e6)
