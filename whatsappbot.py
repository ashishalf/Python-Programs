import pyautogui as pg
import time

time.sleep(10)

for i in range(50):
    pg.write("Hello Dear")
    pg.press("Enter")  