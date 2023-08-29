import pyautogui
import time
import pyperclip
import subprocess


import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

pyautogui.moveTo(999, 231, 0.2)
pyautogui.click()
time.sleep(1)
print("1")
pyperclip.copy("서울날씨")
print("2")
pyautogui.hotkey("command", "v")
time.sleep(1)
print("3")

pyautogui.write(["enter"])
time.sleep(1)

start_x = 766
start_y = 283
end_x = 1420
end_y = 688

pyautogui.screenshot(r'Seoul_weather.png', region=(start_x,start_y,end_x-start_x, end_y-start_y))
# pyautogui.screenshot(r'P10_automouse/Seoul_weather.png', region=(766,283,1420-766,688-283))

print("4")
