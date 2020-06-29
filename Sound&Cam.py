from gpiozero import LED
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import picamera
import time

red_led = LED(18)

pir = MotionSensor(4)

camera = picamera.PiCamera()

mic = 17
camera.vflip = True

def Sound_tick(mic):
    if GPIO.input(mic) is GPIO.HIGH:
        camera.start_recording('Slap.h264')
        time.sleep(10)
        camera.stop_recording()
        pir.wait_for_no_motion()
        
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.add_event_detect(mic, GPIO.BOTH, bouncetime = 500)
GPIO.add_event_callback(mic, Sound_tick)

while True:
    pir.wait_for_motion()
    print('Motion Detected.')
    time.sleep(3)
    