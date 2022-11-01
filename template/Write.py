from asyncore import write
import time
import random
from tkinter import E
import pyautogui

time.sleep(5)
text = 'I want to write Something!'
for _ in range(3):
    pyautogui.typewrite(text,interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.1)

