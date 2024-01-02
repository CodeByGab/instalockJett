import time
import pyautogui as pg
import keyboard as kb

time.sleep(2)

pg.PAUSE = 0.01 
pg.FAILSAFE = True

#Run the script untill you press key '1'
def check_ket():
    return kb.is_pressed('1')

while not check_ket():
    pg.moveTo(922, 590, duration=0.1)
    pg.click(duration=0.1)

    pg.moveTo(685, 519, duration=0.1)
    pg.click(duration=0.1)