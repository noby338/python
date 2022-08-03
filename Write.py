import time
import random
from tkinter import E
import pyautogui

time.sleep(5)
text = 'Something I want to write'
for _ in range(20):
    pyautogui.typewrite(text,interval=0.1)
    pyautogui.press('enter')
    # time.sleep(0.1)
