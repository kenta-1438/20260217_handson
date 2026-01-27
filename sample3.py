import pyautogui as pag
import keyboard as kb
import sys

while True:
    pos=pag.position()
    print(pos)
    if kb.is_pressed("Escape"):
        sys.exit()
    pag.sleep(1)