import pyautogui

for n in range(10):
    pos=pyautogui.position()
    print(n,pos)
    pyautogui.sleep(1)