import pyautogui
from time import sleep
import os
from tqdm import tqdm


def Posicao():
    global seta_x
    global seta_y
    global remover_x
    global remover_y
    global botao_rem_x
    global botao_rem_y

    print("| COLOQUE O MOUSE NA POSIÇÃO PARA CAPTURA |")
    print("Posicao atual do mouse ícone seta..")
    sleep(5)
    seta_x, seta_y = pyautogui.position()
    print("x = " + str(seta_x) + " y = " + str(seta_y))
    print("Posicao atual do mouse opção de remover..")
    sleep(3)
    remover_x, remover_y = pyautogui.position()
    print("x = " + str(remover_x) + " y = " + str(remover_y))
    print("Posicao atual do mouse botão de remover..")
    sleep(3)
    botao_rem_x, botao_rem_y = pyautogui.position()
    print("x = " + str(botao_rem_x) + " y = " + str(botao_rem_y))
    print("Retornando ao Menu Principal...")
    sleep(2)
    Menu()


def BanAll():
    global seta_x
    global seta_y
    global remover_x
    global remover_y
    global botao_rem_x
    global botao_rem_y

    print("| Qual será a quantidade de BAN ?")
    total_ban = int(input("> "))
    result = 0
    for j in tqdm(range(total_ban)):
        result += j
        sleep(0.5)
    for i in range(total_ban):
        pyautogui.moveTo(seta_x, seta_y)  # vai ate o botao de abrir opçoes
        sleep(0.9)
        pyautogui.click(seta_x, seta_y)  # botao de abrir opcoes
        sleep(0.5)
        pyautogui.click(remover_x, remover_y)  # opção de remover
        sleep(0.5)
        pyautogui.click(botao_rem_x, botao_rem_y)  # botao de remover
        sleep(1.5)
        os.system("cls")
        print("QUANTIDADE DE REMOÇÕES: {}".format(i + 1))
    print("Retornando ao Menu Principal...")
    sleep(2)
    Menu()


def Menu():
    os.system("cls")
    print(
        """
        | Escolha uma opção |
          
          [1] - Capturar posição do Mouse
          [2] - Iniciar BAN
          [0] - Sair
          """
    )
    op = int(input(">"))
    if op == 1:
        Posicao()
    elif op == 2:
        BanAll()
    elif op == 0:
        print("Encerrando programa...")
        sleep(3)
    else:
        print("Opcao Invalida")
        Menu()


Menu()
