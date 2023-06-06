from time import sleep
import os

quantidade_tarefas = 0
limite_tarefas = 10
tarefas = []

def AdicionarTarefa():

    global quantidade_tarefas

    print('< ADICIONAR TAREFAS >')
    if quantidade_tarefas < limite_tarefas:
        nome_tarefa = str(input('Digite o nome da tarefa: '))
        tarefas.append(nome_tarefa)
        sleep(1)
        quantidade_tarefas += 1
        print('Tarefa Adicionada com sucesso')
        sleep(1)
        os.system('cls')
        Menu()

    else:
        print('Limite máximo de tarefas foi atingido.')
        sleep(1)
        os.system('cls')
        Menu()

def RemoverTarefa():

    global quantidade_tarefas

    if quantidade_tarefas > 0:
        print('< ESCOLHA A TAREFA QUE DESEJA REMOVER. >')
        print(' ')
        for i in range(len(tarefas)):
            print(f'[{i+1}] - {tarefas[i]}')
        op = int(input('> '))
        if op >= i and op <= len(tarefas):
            tarefa_removida = tarefas.pop(op-1)
            quantidade_tarefas -= 1
            print(f'Tarefa "{tarefa_removida}" removida com sucesso.')
            sleep(1)
            os.system('cls')
            Menu()
        else:
            print('Não existe essa tarefa listada.')
            sleep(1)
            os.system('cls')
            Menu()
    else:
        print('Não existem tarefas listadas..')
        sleep(1)
        os.system('cls')
        Menu()

def ListarTarefas():

    global quantidade_tarefas

    if quantidade_tarefas > 0:
        print('< LISTA DE TAREFAS >')

        for i in range(len(tarefas)):
            print(f'[{i+1}] - {tarefas[i]}')

        print('''
            
            [1] - Adicionar Tarefa
            [2] - Remover Tarefa
            [0] - Voltar ao Menu
        
        ''')
        op = int(input('> '))
        os.system('cls')
        if op == 1:
            AdicionarTarefa()
        elif op == 2:
            RemoverTarefa()
        elif op == 0: 
            Menu()
    else: 
        print('< Você ainda não adicionou nenhuma tarefa.')
        print('Deseja adicionar ? (S/N)')
        op = str(input('> ')).lower()
        os.system('cls')
        if op == 's':
            AdicionarTarefa()
        elif op == 'n':
            Menu()
        else:
            print('Comando inválido..')
            Menu()

def Menu():

    print('''
        | GERENCIADOR DE TAREFAS |
        
        [1] - Adicionar Tarefa
        [2] - Remover Tarefa
        [3] - Listar Tarefas
        [0] - Sair
        ''')
    op = int(input('> '))
    os.system('cls')
    if op == 1:
        AdicionarTarefa()
    elif op == 2:
        RemoverTarefa()
    elif op == 3:
        ListarTarefas()
    elif op == 0:
        print('Encerrando gerenciador de tarefas...')
        sleep(2)
    else:
        print('Comando inválido !')
        Menu()
Menu()
