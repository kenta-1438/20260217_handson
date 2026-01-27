#ブラウザを起動して,サイトにアクセスする。
#
#【手順】
#1. ブラウザの実行ファイル（.exe）の場所を予め確認しておく。
#2. アクセスしたいサイトのURLを確認し,プログラムの10行目にペーストする。

import subprocess

app="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"   # Google Chrome 実行ファイルの場所 
URL="https://www.yahoo.co.jp/"   # アクセスしたいサイトのURL (ここでは, Yahoo! JAPAN) 

subprocess.Popen([app,URL])
