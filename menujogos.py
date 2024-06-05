from time import sleep
import random
import os
from colorama import Fore, Back, Style


def Multiplicacao():
    acertos = 0
    erros = 0
    os.system("cls")
    tentativas = 10
    print(
        f"""     
         [JOGO DA MULTIPLICAÇÃO]
    ---------------------------------
    Tente descobrir qual é o resultado...

    -> Você tem [{tentativas}] perguntas. Quantas consegue acertar?
    """
    )

    for i in range(tentativas):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        resultado = n1 * n2
        resposta = int(input(f"Quanto é {n1} x {n2} ? "))
        if resposta == resultado:
            print("Analisando Resposta!")
            sleep(1)
            print(Fore.GREEN + "-> Você acertou !" + Fore.RESET)
            acertos += 1
        else:
            print("Analisando Resposta!")
            sleep(1)
            print(Fore.RED + "-> Você errou" + Fore.RESET)
            erros += 1
    sleep(1)
    print(f"Você obteve:  {acertos} acerto(s).")
    print(f"Você obteve: {erros} erro(s).")
    print("Deseja jogar novamente ? (s/n)")
    op = str(input("-> ")).lower()
    if op == "s":
        Multiplicacao()
    elif op == "n":
        print("Obrigado, volte sempre !")
        sleep(5)
        Jogo()
    else:
        print("Opção Inválida.")


def Jokenpo():
    os.system("cls")
    opcoes = ["Pedra", "Papel", "Tesoura"]
    print(" ")
    print("---- JO KEN PO ----")
    print("Seja Bem Vindo(a) !")
    player = int(
        input(
            """

    Escolha uma opção:

    [0] - Pedra
    [1] - Papel
    [2] - Tesoura
    
    -> """
        )
    )
    bot = random.randint(0, 2)

    if opcoes[player] == opcoes[bot]:
        print("-> PLAYER: ", opcoes[player])
        print("-> CPU: ", opcoes[bot])
        print("[ EMPATE ]")

    elif (
        opcoes[player] == "Pedra"
        and opcoes[bot] == "Tesoura"
        or opcoes[player] == "Papel"
        and opcoes[bot] == "Pedra"
        or opcoes[player] == "Tesoura"
        and opcoes[bot] == "Papel"
    ):
        print("-> PLAYER: ", opcoes[player])
        print("-> CPU: ", opcoes[bot])
        print("[ PLAYER - VENCEU !]")

    elif (
        opcoes[bot] == "Pedra"
        and opcoes[player] == "Tesoura"
        or opcoes[bot] == "Papel"
        and opcoes[player] == "Pedra"
        or opcoes[bot] == "Tesoura"
        and opcoes[player] == "Papel"
    ):
        print("-> PLAYER: ", opcoes[player])
        print("-> CPU: ", opcoes[bot])
        print("[ CPU - VENCEU !]")
    print(" ")
    print("Deseja jogar novamente ? (s/n)")
    op = str(input("-> ")).lower()
    if op == "s":
        Jokenpo()
    elif op == "n":
        Jogo()


def Dados():
    os.system("cls")
    tentativas = 3
    print(
        """--- JOGO DOS DADOS IGUAIS ---

    #você tem 3 tentativas.

    Escolha uma opção: 
    1 - Jogar Dados
    2 - Sair
    """
    )
    op = int(input("-> "))

    for i in range(tentativas):
        if op == 1:
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            if dado1 == dado2:
                os.system("cls")
                print(
                    f"""
                    Dado 1: {dado1}
                    Dado 2: {dado2}
                
                """
                )

                print(Fore.GREEN + "PARABÉNS - OS DADOS FORAM IGUAIS" + Fore.RESET)
                sleep(2)
                print("Deseja jogar novamente ? (s/n)")
                op = input("> ").lower()
                if op == "s":
                    Dados()
                elif op == "n":
                    Jogo()
            else:
                print(
                    f"""
                    Dado 1: {dado1}
                    Dado 2: {dado2}

                """
                )

                print("Jogar Novamente? (s/n)")
                esc = str(input("> "))
                tentativas = tentativas - 1
                print("-> Não foram Iguais")
                print("-> Restam {} tentativa(s)".format(tentativas))
                if esc == "s":
                    if tentativas == 0:
                        print("Suas tentativas acabaram ! ")
                        print(Fore.RED + "GAME OVER ! " + Fore.RESET)
                        sleep(2)
                        print("Deseja jogar novamente ? (s/n)")
                        op = input("> ").lower()
                        if op == "s":
                            Dados()
                        elif op == "n":
                            Jogo()
                continue
        else:
            print("Obrigado por Jogar - Volte Sempre !")
            sleep(2)
            Jogo()


def JogoVelha():
    global tabuleiro
    global jogadas
    global jogarNovamente
    global quemJoga
    global maxJogadas
    global vitoria

    os.system("cls")
    jogarNovamente = "s"
    jogadas = 0
    quemJoga = 2  # 1 - CPU / 2 - Jogador
    maxJogadas = 9
    vitoria = "n"
    tabuleiro = [
        [" ", " ", " "],  # L0C0  L0C1  L0C1
        [" ", " ", " "],  # L1C0  L1C1  L1C2
        [" ", " ", " "],  # L2C0  L2C1  L2C2
    ]

    def Tela():
        global tabuleiro
        global jogadas

        os.system("cls")

        print("    0   1   2")
        print(
            "0:  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2]
        )
        print("   ------------")
        print(
            "1:  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2]
        )
        print("   ------------")
        print(
            "2:  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2]
        )
        print("   ------------")
        print(" ")
        print("> Jogadas: " + str(jogadas))

    def JogadorJoga():
        global jogadas
        global quemJoga
        global vitoria
        global maxJogadas

        if quemJoga == 2 and jogadas < maxJogadas:
            try:
                linha = int(input("> Linha: "))
                coluna = int(input("> Coluna: "))
                while tabuleiro[linha][coluna] != " ":
                    print("Espaço Indisponível - Escolha novamente !")
                    linha = int(input("> Linha: "))
                    coluna = int(input("> Coluna: "))

                tabuleiro[linha][coluna] = "X"
                quemJoga = 1
                jogadas += 1

            except:
                print("Jogada Inválida.")
                os.system("pause")

    def CPUJoga():
        global jogadas
        global quemJoga
        global maxJogadas

        if quemJoga == 1 and jogadas < maxJogadas:
            if jogadas == 0:
                linha = random.randrange(0, 3)
                coluna = random.randrange(0, 3)
            else:
                (linha, coluna) = encontrarMelhorJogada()

            tabuleiro[linha][coluna] = "O"
            jogadas += 1
            quemJoga = 2

    def verificarVitoria():
        # tabuleiro[0][0]  tabuleiro[0][1]  tabuleiro[0][2])
        # tabuleiro[1][0] tabuleiro[1][1]  tabuleiro[1][2])
        # tabuleiro[2][0]  tabuleiro[2][1]  tabuleiro[2][2])
        global tabuleiro
        win = "n"
        simbolos = ["X", "O"]
        for s in simbolos:
            win = "n"
            # verificar vitoria em linhas
            indiceLinhas = indiceColunas = 0
            while indiceLinhas < 3:
                soma = 0
                indiceColunas = 0
                while indiceColunas < 3:
                    if tabuleiro[indiceLinhas][indiceColunas] == s:
                        soma += 1
                    indiceColunas += 1
                indiceLinhas += 1
                if soma == 3:
                    win = s
                    break
                indiceLinhas += 1
            if win != "n":
                break
            # verificar colunas
            indiceLinhas = indiceColunas = 0
            while indiceColunas < 3:
                soma = 0
                indiceLinhas = 0
                while indiceLinhas < 3:
                    if tabuleiro[indiceLinhas][indiceColunas] == s:
                        soma += 1
                    indiceLinhas += 1
                if soma == 3:
                    win = s
                    break
                indiceColunas += 1
            if win != "n":
                break

            # verificar diagonais 1
            soma = 0
            indiceDiagonal = 0
            while indiceDiagonal < 3:
                if tabuleiro[indiceDiagonal][indiceDiagonal] == s:
                    soma += 1
                indiceDiagonal += 1
            if soma == 3:
                win = s
                break

            # verificar diagonais 2
            soma = 0
            indiceDiagonal_Linha = 0
            indiceDiagonal_Coluna = 2
            while indiceDiagonal_Linha < 3:
                if tabuleiro[indiceDiagonal_Linha][indiceDiagonal_Coluna] == s:
                    soma += 1
                indiceDiagonal_Linha += 1
                indiceDiagonal_Coluna -= 1
            if soma == 3:
                win = s
                break
        return win

    def Redefinir():
        global tabuleiro
        global jogadas
        global jogarNovamente
        global quemJoga
        global maxJogadas
        global vitoria

        jogarNovamente = "s"
        jogadas = 0
        quemJoga = 2  # 1 - CPU / 2 - Jogador
        maxJogadas = 9
        vitoria = "n"
        tabuleiro = [
            [" ", " ", " "],  # L0C0  L0C1  L0C1
            [" ", " ", " "],  # L1C0  L1C1  L1C2
            [" ", " ", " "],  # L2C0  L2C1  L2C2
        ]

    def pontuacao(estado):
        if estado == "X":
            return -1
        elif estado == "O":
            return 1
        else:
            return 0

    def minimax(tabuleiro, profundidade, maximizando):
        resultado = verificarVitoria()

        if resultado != "n":
            return pontuacao(resultado)

        if maximizando:
            melhorPontuacao = float("-inf")
            for linha in range(3):
                for coluna in range(3):
                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = "O"
                        valorPontuacao = minimax(tabuleiro, profundidade + 1, False)
                        tabuleiro[linha][coluna] = " "
                        melhorPontuacao = max(valorPontuacao, melhorPontuacao)
            return melhorPontuacao
        else:
            melhorPontuacao = float("inf")
            for linha in range(3):
                for coluna in range(3):
                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = "X"
                        valorPontuacao = minimax(tabuleiro, profundidade + 1, True)
                        tabuleiro[linha][coluna] = " "
                        melhorPontuacao = min(valorPontuacao, melhorPontuacao)
            return melhorPontuacao

    def encontrarMelhorJogada():
        melhorPontuacao = float("-inf")
        melhorJogada = None

        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = "O"
                    pontuacao = minimax(tabuleiro, 0, False)
                    tabuleiro[linha][coluna] = " "
                    if pontuacao > melhorPontuacao:
                        melhorPontuacao = pontuacao
                        melhorJogada = (linha, coluna)

        return melhorJogada

    while True:
        Tela()
        JogadorJoga()
        vitoria = verificarVitoria()
        if vitoria != "n" or jogadas >= maxJogadas:
            break
        CPUJoga()
        Tela()
        vitoria = verificarVitoria()
        if vitoria != "n" or jogadas >= maxJogadas:
            break

    print("Jogador : [" + vitoria + "] Ganhou  !")
    print("Jogadas: " + str(jogadas))


def Jogo():
    os.system("cls")
    print(
        """
        > [ MENU DE JOGOS ] <

        1 - JOGO DO CÁLCULO
        2 - JO KEN PO
        3 - DADOS
        4 - JOGO DA VELHA
        9 - SAIR
        """
    )
    op = int(input("Escolha uma opção: "))
    if op == 1:
        Multiplicacao()
    elif op == 2:
        Jokenpo()
    elif op == 3:
        Dados()
    elif op == 4:
        JogoVelha()
    elif op == 9:
        print("OBRIGADO POR JOGAR - VOLTE SEMPRE !")
        sleep(1)
    else:
        print("Opção Inválida.")
        sleep(1)
        Jogo()
    sleep(2)


Jogo()
