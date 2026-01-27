#メモ帳に書かれている文字「123」をコピーして,5回ペーストする。
#【手順】
#1. メモ帳を開いて,半角英数で「123」と入力する。
#2. sampla3.pyを動かして,「123」の画面上の座標を確認し,プログラムを修正する。
#3. メモ帳のウィンドウの場所をそのままにして,プログラムを実行する。


import pyautogui as pag

#文字をコピー
pag.moveTo(2555,243,duration=1)
pag.dragTo(2589,243,duration=1,button="left")
pag.hotkey("ctrl","c")

#改行
pag.click(2589,243,duration=1)
pag.press("Enter")

#5回ペースト
for i in range(5):
    pag.hotkey("ctrl","v")
    pag.press("Enter")
    