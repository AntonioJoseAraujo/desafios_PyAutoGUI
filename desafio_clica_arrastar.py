import pyautogui
# Move os arquivos para outra pasta
for i in range(3):
    pyautogui.moveTo(1301, 167, duration=0.5)
    pyautogui.dragTo(1045, 588, button='left', duration=0.5)
# Entra na outra pasta
pyautogui.doubleClick(1080, 157, button='left', duration=1)
# Pega os arquivos e volta para a pasta anterior e depois entra na pasta
for i in range(3):
    pyautogui.moveTo(862, 155, duration=0.5)
    pyautogui.dragTo(869, 71, button='left', duration=1)
pyautogui.click()

print('Fim do programa!')
