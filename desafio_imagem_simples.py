import pyautogui

captcha = pyautogui.locateCenterOnScreen('google.png')
pyautogui.click(captcha[0],captcha[1], duration=1)