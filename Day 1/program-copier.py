import pyautogui
import sys
import time
import subprocess
import random


with open(sys.argv[0], mode="r") as f:
    s = f.read()

name = "untitled"+str(random.randint(1, 1000))+".py"
subprocess.Popen("notepad.exe")
time.sleep(1)
pyautogui.typewrite(s, 0.1)
pyautogui.hotkey("ctrl", "s")
time.sleep(0.6)
pyautogui.typewrite(name, 0.1)
pyautogui.press("enter")
time.sleep(0.6)
pyautogui.hotkey("alt", "f4")
