#PCの表示画面の中から,あらかじめ登録しておいた画像（ここでは, Excel.png とする）が
#表示されている部分を探して,ダブルクリックする。OpenCVを使用する方法。
#
#【手順】
#1. pip install pillow opencv-python を実行する。
#2. Microsoft Excelを起動して,Excel.pngが表示されている画面を出しておく。

import cv2
import pyautogui as pag
import numpy as np
import time
import pyscreeze
from PIL import Image

time.sleep(2)

# スクリーンショットを取得
screenshot = pag.screenshot()

# PIL形式 → OpenCV形式に変換
screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# 探したい画像ファイル
template = cv2.imread("Excel.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# スクリーンショットもグレースケールに
screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

# テンプレートマッチング
result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# マッチ度の閾値
threshold = 0.35
if max_val >= threshold:
    # マッチした位置の中心座標を計算
    t_height, t_width = template_gray.shape
    center_x = max_loc[0] + t_width // 2
    center_y = max_loc[1] + t_height // 2

    # クリック
    pag.moveTo(center_x, center_y, duration=0.5)
    pag.doubleClick()
    print(f"クリックしました: ({center_x}, {center_y})")
else:
    print("ボタンが見つかりませんでした")