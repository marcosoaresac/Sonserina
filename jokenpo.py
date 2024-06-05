import random

opcoes = ['Pedra','Papel','Tesoura']

player1 = random.randint(0,2)
player2 = random.randint(0,2)

if opcoes[player1] == opcoes[player2]:
    print('-> PLAYER 1: ',opcoes[player1])
    print('-> PLAYER 2: ',opcoes[player2])
    print('[ EMPATE ]')

elif opcoes[player1] == 'Pedra' and opcoes[player2] == 'Tesoura' or opcoes[player1] == 'Papel' and opcoes[player2] == 'Pedra' or opcoes[player1] == 'Tesoura' and opcoes[player2] == 'Papel':
    print('-> PLAYER 1: ',opcoes[player1])
    print('-> PLAYER 2: ',opcoes[player2])
    print('[ PLAYER 01 - VENCEU !]')

elif opcoes[player2] == 'Pedra' and opcoes[player1] == 'Tesoura' or opcoes[player2] == 'Papel' and opcoes[player1] == 'Pedra' or opcoes[player2] == 'Tesoura' and opcoes[player1] == 'Papel':
    print('-> PLAYER 1: ',opcoes[player1])
    print('-> PLAYER 2: ',opcoes[player2])
    print('[ PLAYER 02 - VENCEU !]')