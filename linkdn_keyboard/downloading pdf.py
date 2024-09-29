import pyautogui
import time

pyautogui.PAUSE = 2
next = (555, 540)
save = (1154, 655)
save2 = (746, 435)
min = (1189, 28 )

time.sleep(10)
for i in range(4):
    pyautogui.keyDown('ctrl')
    pyautogui.press('p')
    pyautogui.keyUp('ctrl')
    time.sleep(2)
    pyautogui.click(save)
    time.sleep(2)
    pyautogui.click(save2)
    time.sleep(2)
    pyautogui.click(next)
    time.sleep(2)
