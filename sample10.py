import pyautogui as pag
import time

p = pag.locateOnScreen("Excel.png",confidence=0.35)
x,y=pag.center(p)
time.sleep(1)
pag.doubleClick(x,y,button="left")
