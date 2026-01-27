# プログラム開始時のマウスカーソルの場所を取得する。
# 続いて1秒かけて,(300,300)にマウスカーソルを移動する。

import pyautogui as pag

print(f"移動前:{pag.position()}")
pag.moveTo(300,300,duration=1)

print(f"移動後:{pag.position()}")
