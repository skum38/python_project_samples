import pyautogui
import time

# Open Notepad
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite('notepad', interval=0.05)
pyautogui.press('enter')
time.sleep(1)

# Type content into the file
pyautogui.typewrite('Did you see me writing my_file.txt' \
'', interval=0.02)

# Save the file
pyautogui.hotkey('ctrl', 's')
time.sleep(0.5)


# Type filename
pyautogui.typewrite('my_file.txt', interval=0.05)
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl', 'W')
print("File created and saved successfully!")