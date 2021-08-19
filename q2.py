from os import popen
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, WINDOW_CLOSED, Window, popup

def salvar_dados(nome, idade, email):
    f = open(f"usuarios.txt", "a")
    usuario_nome = nome
    usuario_nome = usuario_nome.replace(' ', '')
    f.write(f"{usuario_nome} ")
    f.write(f"{idade} ")
    f.write(f"{email}")
    f.write("\n")
    f.close()

def janela_principal():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Insira seus dados para serem salvos em um arquivo .txt!')],
        [sg.Text('Nome: '), sg.Input(key='Nome', border_width=2)],
        [sg.Text('Idade: '), sg.Input(key='Idade', border_width=2)],
        [sg.Text('Email: '), sg.Input(key='Email', border_width=2)],
        [sg.Button('Salvar'), sg.Button('Usuarios Salvos')]
    ]
    return sg.Window('Salvar Dados', layout=layout, finalize= True)

usuarios = []
idades = []
emails = []
try:
    f = open("usuarios.txt", "r")
    while True:
        linha = f.readline()
        usuario = linha.split()
        if usuario != "":
            usuarios.append(usuario[0])
            idades.append(usuario[1])
            emails.append(usuario[2])
        else:
            break

except:
    f = open("usuarios.txt", 'a')
    

def tela_usuarios():
    sg.theme('Reddit')
    layout=[
            [sg.Text('Usuários salvos:', font='Lucida',justification='left')],
            [sg.Listbox(values=usuarios, select_mode='extended', key='fac', size=(30, 6))],
            [sg.Button('Exibir')]]
    return sg.Window('Usuários', layout=layout, finalize=True)


def salvar():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Dados Salvos')],
        [sg.Button('Fechar')]
    ]
    return sg.Window('Dados Salvos', layout=layout, finalize=True)

janela2, janela_salvar, janela_usuarios = janela_principal(), None, None

while True:
    window, event, values = sg.read_all_windows()

    print(usuarios)
    print(emails)
    print(idades)

    if event == WINDOW_CLOSED:
        break
    if window == janela2 and event == 'Salvar':
        nome = values['Nome']
        idade = values['Idade']
        email = values['Email']
        salvar_dados(nome, idade, email)
        janela_salvar = salvar()

    if event == 'Usuarios Salvos':
        try:
            f = open("usuarios.txt", "r")
            while True:
                linha = f.readline()
                usuario = linha.split()
                if usuario != "":
                    usuarios.append(usuario[0])
                    idades.append(usuario[1])
                    emails.append(usuario[2])
                else:
                    break

        except:
            f = open("usuarios.txt", 'a')

        janela_usuarios = tela_usuarios()

    if event == 'Exibir':
        e, v = janela_usuarios.read()
        usuario_nome = v['fac'][0]
        usuario_nome = usuario_nome.replace('[', '')
        usuario_nome = usuario_nome.replace(']', '')
        usuario_nome = usuario_nome.replace("'", '')
        index = usuarios.index(usuario_nome)

        usuario_idade = idades[index]
        usuario_email = emails[index]

        usuario_idade = usuario_idade.replace("'", '')
        usuario_idade = usuario_idade.replace("'", '')
        usuario_idade = usuario_idade.replace("'", '')
        usuario_email = usuario_email.replace("'", '')
        usuario_email = usuario_email.replace("'", '')
        usuario_email = usuario_email.replace("'", '')
        usuario_email = usuario_email.replace("\n", '')
        sg.popup(f"Nome: {usuario_nome}, Idade: {usuario_idade}, Email: {usuario_email}")
    

    if event == 'Fechar':
        janela_salvar.close()