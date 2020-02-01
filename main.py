from gpiozero import Button
import time
import sys
from debouncer import *
#from test1 import *
#from test.test2 import *
#import caption
#import webcam.py
import threading

sys.path.append('/home/pi/Desktop/ETA/pydnet-master/pydnet-master/') 
#add pydnet folder to sys.path so that we can import pydnet files directly
sys.path.append('/home/pi/Desktop/ETA/test/')
#test path

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Important pins (Broadcomm notation)
trigger_get_caption = 17
trigger_toggle_depth = 27

trigger_volume_up = 15
trigger_volume_down = 18

trigger_shutdown = 22
#trigger_restart = 17

button_get_caption = Button(trigger_get_caption)
button_toggle_depth = Button(trigger_toggle_depth)
button_volume_up = Button(trigger_volume_up)
button_volume_down = Button(trigger_volume_down)
button_shutdown = Button(trigger_shutdown)
allowed_delay = 2 #in seconds
volume_allowed_delay = 0.1
#print("Running")

print("Running")


get_caption_time = 0.0
def get_caption():
    start = time.time()
    global get_caption_time 
    if(start - get_caption_time < allowed_delay):
        get_caption_time = start
        return
    print("image caption")
    print(trigger_get_caption)
    #print(caption.get_caption())
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
    print()
    get_caption_time = start

toggle_depth_time = 0.0
def toggle_depth():
    start = time.time()
    global toggle_depth_time
    if(start - toggle_depth_time < allowed_delay):
        toggle_depth_time = start
        return
    print("toggle depth")
    print(trigger_toggle_depth)
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
    print()
    toggle_depth_time = start

volume_up_time = 0.0
def volume_up():
    start = time.time()
    global volume_up_time 
   # if(start - volume_up_time < volume_allowed_delay):
    #    volume_up_time = start
    #    return
    print("volume up")
    print(trigger_volume_up)
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
    print()
    volume_up_time = start

volume_down_time = 0.0
def volume_down():
    start = time.time()
    global volume_down_time
   # if(start - volume_down_time < volume_allowed_delay):
    #    volume_down_time = start
    #    return 
    print("volume down")
    print(trigger_volume_down)
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
    print()
    volume_down_time = start


def shutdown():
    start = time.time()
    print("shutdown")
    print(trigger_shutdown)
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
    print()

def restart():
    start = time.time()
    print("restart")
    end = time.time()
    print("{0} seconds elapsed".format(end - start))
    print()




button_get_caption.when_pressed = get_caption
button_toggle_depth.when_pressed  = toggle_depth
button_volume_up.when_pressed  = volume_up
button_volume_down.when_pressed  = volume_down
button_shutdown.when_pressed  = shutdown

button_get_caption.wait_for_press()
button_toggle_depth.wait_for_press()
button_volume_up.wait_for_press()
button_volume_down.wait_for_press()
button_shutdown.wait_for_press()
#GPIO.setup([trigger_get_caption, trigger_toggle_depth, trigger_volume_up, trigger_volume_down, trigger_shutdown, trigger_restart], GPIO.IN, pull_up_down=GPIO.PUD_UP)

#cb1 = ButtonHandler(trigger_get_caption, get_caption, edge='falling', bouncetime=100)
#cb1.start()

#cb2 = ButtonHandler(trigger_toggle_depth, toggle_depth, edge='falling', bouncetime=100)
#cb2.start()

#cb3 = ButtonHandler(trigger_volume_up, volume_up, edge='falling', bouncetime=100)
#cb3.start()

#cb4 = ButtonHandler(trigger_volume_down, volume_down, edge='falling', bouncetime=100)
#cb4.start()

#cb5 = ButtonHandler(trigger_shutdown, shutdown, edge='falling', bouncetime=100)
#cb5.start()

#cb6 = ButtonHandler(trigger_restart, restart, edge='falling', bouncetime=100)
#cb6.start()

#GPIO.add_event_detect(trigger_get_caption, GPIO.FALLING, callback=get_caption)
#GPIO.add_event_detect(trigger_toggle_depth, GPIO.FALLING, callback=toggle_depth)
#GPIO.add_event_detect(trigger_volume_up, GPIO.FALLING, callback=volume_up)
#GPIO.add_event_detect(trigger_toggle_depth, GPIO.FALLING, callback=toggle_depth)
#GPIO.add_event_detect(trigger_volume_up, GPIO.FALLING, callback=volume_up)
#GPIO.add_event_detect(trigger_volume_down, GPIO.FALLING, callback=volume_down)
#GPIO.add_event_detect(trigger_shutdown, GPIO.FALLING, callback=shutdown)

