from time import sleep
import os
import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init("sapi5")
voices = maquina.getProperty("voices")
maquina.setProperty("voice", voices[0].id)

frases = []
quantidade_frases = 15
frases_inclusas = 0


def AdicionarFrase():
    global quantidade_frases

    print("< ADICIONAR frases >")
    if frases_inclusas < quantidade_frases:
        nome_Frase = str(input("Digite o nome da Frase: "))
        frases.append(nome_Frase)
        sleep(1)
        quantidade_frases += 1
        print("Frase Adicionada com sucesso")
        sleep(1)
        os.system("cls")
        Menu()

    else:
        print("Limite máximo de frases foi atingido.")
        sleep(1)
        os.system("cls")
        Menu()


def RemoverFrase():
    global quantidade_frases

    if quantidade_frases > 0:
        print("< ESCOLHA A FRASE QUE DESEJA REMOVER. >")
        print(" ")
        for i in range(len(frases)):
            print(f"[{i+1}] - {frases[i]}")
        op = int(input("> "))
        if op >= i and op <= len(frases):
            frase_removida = frases.pop(op - 1)
            quantidade_frases -= 1
            print(f'Frase "{frase_removida}" removida com sucesso.')
            sleep(1)
            os.system("cls")
            Menu()
        else:
            print("Não existe essa Frase listada.")
            sleep(1)
            os.system("cls")
            Menu()
    else:
        print("Não existem frases listadas..")
        sleep(1)
        os.system("cls")
        Menu()


def ListarFrases():
    global quantidade_frases

    if quantidade_frases > 0:
        print("< LISTA DE frases >")

        for i in range(len(frases)):
            print(f"[{i+1}] - {frases[i]}")
        print(
            """
            [1] - Adicionar Frase
            [2] - Remover Frase
            [0] - Voltar ao Menu
        
        """
        )
        op = int(input("> "))
        os.system("cls")
        if op == 1:
            AdicionarFrase()
        elif op == 2:
            RemoverFrase()
        elif op == 0:
            Menu()
    else:
        print("< Você ainda não adicionou nenhuma Frase.")
        print("Deseja adicionar ? (S/N)")
        op = str(input("> ")).lower()
        os.system("cls")
        if op == "s":
            AdicionarFrase()
        elif op == "n":
            Menu()
        else:
            print("Comando inválido..")
            Menu()


def FalarFrase():
    global quantidade_frases

    if quantidade_frases > 0:
        print("< ESCOLHA A FRASE QUE DESEJA FALAR. >")
        print(" ")
        for i in range(len(frases)):
            print(f"[{i+1}] - {frases[i]}")
        op = int(input("> "))
        if op >= i and op <= len(frases):
            frase_escolhida = frases[op - 1]
            print(frase_escolhida)
            maquina.say(frase_escolhida)
            maquina.runAndWait()
            print("Deseja falar outra frase? (s/n)")
            op1 = str(input(">")).lower()
            os.system("cls")
            if op1 == "s":
                FalarFrase()
            elif op1 == "n":
                Menu()
    else:
        print("Não existem frases listadas..")
        sleep(1)
        os.system("cls")
        Menu()


def Menu():
    print(
        """
            | REXY FALA SUAS FRASES |
        *Você pode incluir até 15 frases*
        
        [1] - Adicionar frases
        [2] - Remover frases
        [3] - Listar frases
        [4] - Falar frases
        [0] - Sair
        """
    )
    op = int(input("> "))
    os.system("cls")
    if op == 1:
        AdicionarFrase()
    elif op == 2:
        RemoverFrase()
    elif op == 3:
        ListarFrases()
    elif op == 4:
        FalarFrase()
    elif op == 0:
        print("Encerrando gerenciador de frases...")
        sleep(2)
    else:
        print("Comando inválido !")
        Menu()


Menu()
