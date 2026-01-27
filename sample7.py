#ソフトやアプリケーションの起動

import subprocess
import os

subprocess.Popen('notepad.exe')  #メモ帳を開く。Popen = プログラムとして起動
os.startfile('notepad.exe')      #メモ帳を開く。startfile = 人がダブルクリックしたのと同じ


# アプリケーションの実行ファイルの場所を記述して,以下のようにしてもよい。(コメントアウトしてあります。)

#app='C:/Program Files/Bandicam/bdcam.exe'
#subprocess.Popen(app)
#os.startfile(app)