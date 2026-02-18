import time
import pyautogui as pag

time.sleep(2)
pag.press("win")
time.sleep(1)
pag.write("excel", interval = 0.05)
time.sleep(1)
pag.press("enter")