import pyautogui
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosistion = pyautogui.locateOnScreen('pict1.png')
print(picPosistion)

if picPosistion is None:
    picPosistion = pyautogui.locateOnScreen('pict2.png')
    print(picPosistion)
    