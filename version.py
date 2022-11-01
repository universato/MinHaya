import re

import sys
import csv
import pyautogui as p
import pyperclip
import time as t
import platform

python_info = sys.version.replace("\n", " ")
# python_info = re.sub(" \(.+?\)", "", python_info)

print("Python   ", python_info)
print("csv      ", csv.__version__)
print("pyautogui", p.__version__)
print("pyperclip", pyperclip.__version__)
print("platform ", platform.__version__)
