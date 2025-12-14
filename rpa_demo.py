import time
import pyautogui
print ("Screen size:", pyautogui.size())
pyautogui.moveTo(142, 153, duration=1)
#pyautogui.click()
pyautogui.rightClick()
pyautogui.write('Hello, this is an RPA demo!', interval=0)
time.sleep(4)
x,y=pyautogui.position()
print("Current mouse position:", x, y)



