import RPi.GPIO as GPIO
import time
import sys
#import caption.py
#import webcam.py
import threading

sys.path.append('/home/pi/Desktop/ETA/pydnet-master/pydnet-master/') #add pydnet folder to sys.path so that we can import pydnet files directly
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Important pins (Broadcomm notation)
trigger_get_caption = 15
trigger_toggle_depth = 4

trigger_volume_up = 14
trigger_volume_down = 27

trigger_shutdown = 18
trigger_restart = 17

def get_image_caption(pin):
    print("image caption")
def toggle_depth(pin):
    print("toggle depth")
def volume_up(pin):
    print("volume up")
def volume_down(pin):
    pass
def shutdown(pin):
    pass
def restart(pin):
    pass

GPIO.setup([trigger_get_caption, trigger_toggle_depth, trigger_volume_up, trigger_volume_down, trigger_shutdown, trigger_restart], GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(trigger_get_caption, GPIO.FALLING, get_image_caption)
GPIO.add_event_detect(trigger_toggle_depth, GPIO.FALLING, toggle_depth)
GPIO.add_event_detect(trigger_volume_up, GPIO.FALLING, volume_up)
GPIO.add_event_detect(trigger_volume_down, GPIO.FALLING, volume_down)
GPIO.add_event_detect(trigger_shutdown, GPIO.FALLING, shutdown)
GPIO.add_event_detect(trigger_restart, GPIO.FALLING, restart)

while True:
    time.sleep(1e6)
