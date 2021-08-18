import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, WINDOW_CLOSED, Window

def salvar_dados(nome, idade, email):
    f = open(f"{nome}.txt", "a")
    f.write(f"Nome: {nome}\n")
    f.write(f"Idade: {idade}\n")
    f.write(f"Email: {email}\n")
    f.close()

def janela_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Insira seus dados para serem salvos em um arquivo .txt!')],
        [sg.Text('Nome: '), sg.Input(key='Nome', border_width=2)],
        [sg.Text('Idade: '), sg.Input(key='Idade', border_width=2)],
        [sg.Text('Email: '), sg.Input(key='Email', border_width=2)],
        [sg.Button('Salvar')]
    ]
    return sg.Window('Salvar Dados', layout=layout, finalize= True)

def salvar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Dados Salvos')],
        [sg.Button('Fechar')]
    ]
    return sg.Window('Dados Salvos', layout=layout, finalize=True)

janela2, janela_salvar = janela_principal(), None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela2 and event == WINDOW_CLOSED:
        break
    if window == janela2 and event == 'Salvar':
        nome = values['Nome']
        idade = values['Idade']
        email = values['Email']
        salvar_dados(nome, idade, email)
        janela_salvar = salvar()
        
    if event == 'Fechar':
        break