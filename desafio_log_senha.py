import pyautogui

email = pyautogui.prompt(text='Digite seu e-mail',
                         title='Informações de Login')
senha = pyautogui.password(text='Digite sua senha',
                           title='Informações de Login', mask='*')
pyautogui.click(804, 69, duration=1)
pyautogui.typewrite(email)
pyautogui.press('enter')
pyautogui.typewrite(senha)
