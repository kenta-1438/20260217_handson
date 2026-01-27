#1秒おきにマウスカーソルの場所を取得するのを10回繰り返す

import pyautogui

for n in range(10):
    pos=pyautogui.position()
    print(n,pos)

    pyautogui.sleep(1)
