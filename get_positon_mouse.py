import time
import pyautogui as pg

print("Move the cursor to position you want to get coordinates.")
time.sleep(5)

current_position = pg.position()

print(f"Cursor's position: {current_position}")

# Resolution 1366x768
#jett = X 922
#confirm = x 685, y 519
