import pyautogui
import time

# Delay for 3
time.sleep(5)

# Open a nwe tab
pyautogui.hotkey('ctrl', 't')

# Go to the URL
pyautogui.typewrite("Hello, PyAutoGUI!")

# Search
pyautogui.press('enter')
