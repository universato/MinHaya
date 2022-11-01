# python:cursor.py
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        print('{:.1f}, {:.1f}'.format(x, y))

with Listener(on_click = on_click) as listener:
    listener.join()
