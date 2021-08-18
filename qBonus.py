from random import randint
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, WINDOW_CLOSED, Window
import time

f = open("palavras.txt", "r")
palavras = []

while True:
    palavra = f.readline()
    if palavra != "":
        palavras.append(palavra)
    else:
        break

def principal():
    sg.theme('Reddit')
    layout=[
            [sg.Text('Escolha a palavra para o computador tentar acertar!', font='Lucida',justification='left')],
            [sg.Listbox(values=palavras, select_mode='extended', key='fac', size=(30, 6))],
            [sg.Button('Salvar')]]
    return sg.Window('Principal', layout=layout, finalize=True)

janela = principal()

def chute_computador():
    chute = randint(0,99)
    return chute

while True:
    window, event, values = sg.read_all_windows()

    if window == janela and event == WINDOW_CLOSED:
        break

    if event == 'Salvar':
        chute = chute_computador()
        e, v = janela.read()
        palavra = v['fac'][0]
        palavra = palavra.replace('\n', '')
        palavras[chute] = palavras[chute].replace('\n', '')
        if(palavras[chute] == palavra):
            sg.popup("O computador acertou!!")
        if(palavras[chute] != palavra):
            sg.popup(f"O computador errou!! Ele chutou {palavras[chute]}")