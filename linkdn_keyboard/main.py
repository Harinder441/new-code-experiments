import pyautogui as pg
from time  import sleep


# profile view
Profile_Cordinates = (179, 314)
Scroll_length = -119
Tab_Position = (400, 15)

sleep(5)
for i in range(5):
    pg.keyDown('ctrl')
    pg.click(Profile_Cordinates)
    pg.keyUp('ctrl')
    pg.scroll(Scroll_length)
    sleep(1)
    pg.keyDown('ctrl')
    pg.press('tab')
    pg.keyUp('ctrl')
    sleep(3)
    pg.press('end')
    sleep(1)
    pg.keyDown('ctrl')
    pg.press('w')
    pg.keyUp('ctrl')
    sleep(1)
