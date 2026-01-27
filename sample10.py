# PCの表示画面の中から,あらかじめ登録しておいた画像（ここでは, Excel.png とする）が
# 表示されている部分を探して,ダブルクリックする。

import pyautogui as pag
import time

p = pag.locateOnScreen("Excel.png",confidence=0.35)
x,y=pag.center(p)
time.sleep(1)
pag.doubleClick(x,y,button="left")

