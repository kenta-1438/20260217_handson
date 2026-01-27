import pyautogui as pag

print(f"移動前:{pag.position()}")
pag.moveTo(300,300,duration=1)
print(f"移動後:{pag.position()}")