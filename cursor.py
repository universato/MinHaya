# python:cursor.py
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    print(format(x, '.2f') + ", " + format(y, '.2f'), button, pressed)

with Listener(on_click = on_click) as listener:
    listener.join()
