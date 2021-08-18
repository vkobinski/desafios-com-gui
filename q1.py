from random import randint
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, WINDOW_CLOSED, Window
import time
import os

def randomizar_numero():
    numero_aleatorio = randint(1,100)
    return numero_aleatorio

def janela_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Insira um número de 1 a 100, e tente acertar o que estou pensando!')],
        [sg.Input(key='Tentativa', border_width=2)],
        [sg.Button('Tentar')]
    ]
    return sg.Window('Adivinhe o Número', layout=layout, finalize= True)

def acertou():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você acertou! Parabéns!')],
        [sg.Button('Fechar')]
    ]
    return sg.Window('Acertou!', layout=layout, finalize=True)

def errou(tentativas):
    sg.theme('Reddit')
    layout = [
        [sg.Text('Você errou!')],
        [sg.Text(text=f'Você têm {tentativas} tentativas')],
        [sg.Button('Fechar')]
    ]
    return sg.Window('Errou!', layout=layout, finalize=True)

numero = randomizar_numero()
janela2, janela_acertou, janela_errou = janela_principal(), None, None

tentativas = 3

while True:
    window, event, values = sg.read_all_windows()

    if window == janela2 and event == WINDOW_CLOSED:
        break
    if window == janela2 and event == 'Tentar':
        if int(values['Tentativa']) == int(numero):
            janela_acertou = acertou()
        if int(values['Tentativa']) != int(numero):
            tentativas -= 1
            janela_errou = errou(tentativas)
    if event == 'Fechar':
        if tentativas == 0:
            break
        if janela_acertou != None:
            break
        if janela_errou != None:
            janela_errou.close()
