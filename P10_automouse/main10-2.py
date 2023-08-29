import pyautogui
import time
import pyperclip

pyautogui.moveTo(1218, 211, 0.2)
pyautogui.click()
time.sleep(1)
print("1")
pyperclip.copy("서울날씨")
print("2")
pyautogui.hotkey("command" , "v")
time.sleep(1)
print("3")

pyautogui.write(["enter"])
time.sleep(1)

