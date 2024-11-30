import pyautogui
import pyperclip

def frase(txt):
    pyperclip.copy(txt)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(170,320, duration=1)
frase('Automoção é Incrível!')