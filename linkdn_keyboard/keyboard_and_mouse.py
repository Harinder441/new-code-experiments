import pyautogui
import time

# pyautogui.PAUSE = 0
width,height = pyautogui.size()
print(width,height)


print('Press Ctrl-C to quit.')
try:
    while True: # TODO: Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = '(' + str(x)+ ", "+ str(y)+" )"

        print(positionStr, end='')
        time.sleep(0.1)
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')
