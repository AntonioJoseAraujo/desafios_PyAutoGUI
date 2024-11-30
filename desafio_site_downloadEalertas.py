import pyautogui
import webbrowser
import pyperclip
from time import sleep


def nome_esp(txt):
    pyperclip.copy(txt)
    pyautogui.hotkey('ctrl', 'v')


# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(3)

# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.moveTo(1000, 200, duration=1)
pyautogui.scroll(-2300)
pyautogui.click(814, 360, duration=1)
nome_esp('Antônio José de Araújo')
sleep(1)

# 3) Clique em alerta, para gerar a alerta
ok = pyautogui.locateCenterOnScreen('bot_ok.png')
pyautogui.click(ok[0], ok[1], duration=1)


# 4) Feche a alerta
pyautogui.click(1216, 176, duration=1)
sleep(1)
# 5) Suba a página totalmente para cima
pyautogui.scroll(3000)
sleep(3)
# 6) Desça apenas o suficiente para conseguir chegar até a seção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o download dos arquivos excel e pdf.
pyautogui.scroll(-3900)
pyautogui.click(833, 235, duration=1)
sleep(2)
pyautogui.click(839, 360, duration=1)
sleep(1)
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='Você Terminou', title='Fim da Automação!')
