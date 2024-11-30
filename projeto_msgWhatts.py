import webbrowser
import pyautogui
import pyperclip
from time import sleep


def msg(txt):
    pyperclip.copy(txt)
    pyautogui.hotkey('ctrl', 'v')

# telefones = [554792450000,554794560000,5516997540000]

# Aqui vamos abrir o arquivo txt com os números de telefones e colocar na lista.

telefones = []

with open('fones.txt', 'r') as arquivo:  
    for linha in arquivo:  
        telefones.append(linha.split('\n')[0])
    print(telefones)
for telefone in telefones:
    # aqui vai usar o telefone dessa lista acima
    webbrowser.open(f' https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)  
    # clica no botão para abrir o whatsapp no desktop
    pyautogui.click(762, 204, duration=1)
    sleep(10)
    # digita a msg ja que vai seleciona automaticamente para enviar a msg
    msg('Oi, bom dia... tudo bem? Estou enviando essa msg automatica usando uma automação e seu telefone esta em uma lista para teste. Desculpa pelo incômodo.')
    sleep(5)
    pyautogui.press('enter')  
    sleep(300)  # esse tempo é para que o whatsapp não te bloquei por uso de bot
