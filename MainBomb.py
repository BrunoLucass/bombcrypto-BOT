from pyautogui import *
import pyautogui
from tkinter import *
from tkinter.ttk import *
from pynput.mouse import Button, Controller
from PySimpleGUI import PySimpleGUI as Sg

# import pandas as pd
# import win32com.client as win32

# tempo pra resetar estamina
# ficar abrindo e fechando recompensas ate dar uma hora
#
mouse = Controller()
root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()


def click(coords):
    mouse.position = coords
    sleep(1)
    mouse.click(Button.left, 1)


def movimento(x, y):
    mouse.position = (x, y + 200)
    sleep(1)
    x = 0
    while x < 100:
        mouse.scroll(0, -1)
        sleep(0.1)
        x += 2


def back():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Close.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:  # procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Close.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)  # pega o centro da imagem
            click(coords)
            sleep(0.1)
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)

        else:
            print("nao consigo ver o botao de close")
            sleep(0.5)


def back2():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Back.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:  # procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Back.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)  # pega o centro da imagem
            click(coords)
            sleep(0.1)
            # Close()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)

        elif pyautogui.locateOnScreen('ImagensBomb/Connect2.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Connect2.png', region=(0, 0, width, height),
                                                    grayscale=True,
                                                    confidence=0.8)
            connect2()

        else:
            print("nao consigo ver o botao de back")
            sleep(0.5)


def reset():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Back.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Back.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            hero()  # apos o loop volta para a tela inicial e bota novamente todos bonecos para trabalhar
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de back")
            sleep(0.5)


def menu2():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Menu.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:  # procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Menu.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)  # pega o centro da imagem
            click(coords)
            sleep(2)
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de menu")
            sleep(0.5)


def loop():
    x = 0
    while x < (int(valores['Horas']) / 2):  # espera uma hora
        back2()
        volta()
        sleep(60)
        x += 1
    reset()


def menu():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Menu.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:  # procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Menu.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)  # pega o centro da imagem
            click(coords)
            sleep(2)
            loop()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de menu")
            sleep(0.5)


def volta():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Menu.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:  # procura a imagem na tela
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Menu.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)  # pega o centro da imagem
            click(coords)
            sleep(2)
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)

        elif pyautogui.locateOnScreen('ImagensBomb/Connect2.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            connect2()

        else:
            print("nao consigo ver o botao de volta")
            sleep(0.5)


def close():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Close.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Close.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            menu()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de close")
            sleep(0.5)


def close2():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Close.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Close.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            hero()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False

        else:
            print("nao consigo ver o botao de fechar")
            sleep(0.5)


def works():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/work.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/work.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            x, y = coords
            mouse.position = (x, y)
            coords = x, y + 300
            x = 0
            while x < int(valores['QtdHerois']):
                click(coords)
                print("click")
                x += 1
            sleep(2)
            print("todos trabalhando")
            close()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de work")
            sleep(0.5)


def char():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Character.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Character.png', region=(0, 0, width, height),
                                                    grayscale=True, confidence=0.8)
            x, y = coords
            movimento(x, y)
            sleep(2)
            works()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de character")
            sleep(0.5)


def hero():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Heroes.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Heroes.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            char()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Map.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
        else:
            print("nao consigo ver o botao de herois")
            sleep(0.5)


def assinar():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Assinar.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Assinar.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            hero()
            stop = False
        elif pyautogui.locateOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                      confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/ERROR.png', region=(0, 0, width, height), grayscale=True,
                                                    confidence=0.8)
            click(coords)
            sleep(2)
            connect2()
            stop = False
        else:
            print("nao consigo ver o botao de assinar")
            sleep(0.5)


def connect2():
    stop = True
    while stop:
        if pyautogui.locateOnScreen('ImagensBomb/Connect2.png', region=(0, 0, width, height), grayscale=True,
                                    confidence=0.8) is not None:
            print("consigo ver")
            coords = pyautogui.locateCenterOnScreen('ImagensBomb/Connect2.png', region=(0, 0, width, height),
                                                    grayscale=True, confidence=0.8)
            print(coords)
            click(coords)
            sleep(2)
            assinar()
            stop = False
        else:
            print("nao consigo ver o botao de conectar")
            sleep(0.5)


# defMain():

if __name__ == '__main__':
    # layout
    Sg.theme('Reddit')
    layout = [
        [Sg.Text('Quantos herois voce deseja por em campo por rotação ?'), Sg.Input(key='QtdHerois', size=(20, 1))],
        [Sg.Text('Depois de quantos minutos voce deseja reiniciar o ciclo ?'), Sg.Input(key='Horas', size=(20, 1))],
        [Sg.Button('Iniciar')],
        [Sg.Button('Instruções')]
    ]
    # layout instruções
    Sg.theme('Reddit')
    layout2 = [
        [Sg.Text('1° Certifique se de que seu computador esteja na resolução 1920 x 1080')],
        [Sg.Text('2° Certifique se de que seu computador esteja na escala 100%')],
        [Sg.Text('3° A senha nao sera colocada automaticamente, entao fique atento')],
        [Sg.Text('4° Ao clicar em iniciar basta abrir a pagina do Bomb Crypto e o programa fará o resto')],
        [Sg.Text('5° O programa esta em beta, se tiver sujestões: Discord: Avilactea#1855')],
    ]

    # janela
    janela = Sg.Window('Tela Inicial', layout)
    janela2 = Sg.Window('Instruções', layout2)

    while True:
        eventos, valores = janela.read()
        if eventos == Sg.WINDOW_CLOSED:
            break
        if eventos == 'Iniciar':
            if valores['QtdHerois'] is not None and valores['Horas'] is not None:
                loop()
        if eventos == 'Instruções':
            eventos2 = janela2.read()
            if eventos2 == Sg.WIN_CLOSED:
                break
            # chama o programa levando os valores
    # Close()from pyautogui import *
