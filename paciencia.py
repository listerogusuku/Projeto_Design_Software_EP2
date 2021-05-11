# EP | Exercício Programa: Paciência Acordeão | Design de Software
# Professor: Humberto Sandmann
# Equipe: Celina Vieira de Melo e Lister Ogusuku Ribeiro
# Data: 01/05/2021

#No código a seguir foi feita a implementação do jogo "Paciência Acordeão" (Solitaire Accordion).
#O jogo faz parte do "Exercício Programa 2" da Disciplina Design de Software.

#Neste jogo foram implementadas regras avançadas.

#============================

print('\nPaciência Acordeão\n==================\n\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n\nExistem apenas dois movimentos possíveis:\n\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\n\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n')

import random

def main():
    iniciar = True
    while iniciar == True:
        baralho = cria_baralho()
        while possui_movimentos_possiveis(baralho):          
            a = 0
            while a < len(baralho):
                if extrai_naipe(baralho[a]) == '♥':
                    print('\033[1;97m{0}. \033[1;31m{1}'.format(a+1,baralho[a]))
                if extrai_naipe(baralho[a]) == '♠':
                    print('\033[1;97m{0}. \033[1;32m{1}'.format(a+1,baralho[a]))
                if extrai_naipe(baralho[a]) == '♦':
                    print('\033[1;97m{0}. \033[1;33m{1}'.format(a+1,baralho[a]))
                if extrai_naipe(baralho[a]) == '♣':
                    print('\033[1;97m{0}. \033[1;34m{1}'.format(a+1,baralho[a]))
                a += 1

            carta = int(input('\033[1;97mEscolha uma carta: '))

            carta_no_baralho = baralho[carta-1]
            print('Sua carta é: {}'.format(carta_no_baralho))
            posicao = carta - 1 

            if lista_movimentos_possiveis(baralho,posicao) == [1]:
                print('Você tem 1 movimento possível: mover para a casa anterior!')
                movimento = int(input('Para onde você deseja mover a carta? (primeira anterior: 1 ): '))
                while movimento != 1:
                    print('Movimento inválido')
                    print('Você tem 1 movimento possível: mover para a casa anterior!')
                    movimento = int(input('Para onde você deseja mover a carta? (primeira anterior: 1 ): '))
                
            if lista_movimentos_possiveis(baralho,posicao) == []:
                print('Você não tem movimentos possíveis, tente outra vez!')
                
            if lista_movimentos_possiveis(baralho, posicao) == [3]:
                print('Você tem 1 movimento possível: mover para a terceira casa anterior!')
                movimento = int(input('Para onde você deseja mover a carta? (terceira anterior: 3): '))
                while movimento != 3:
                    print('Movimento inválido')
                    print('Você tem 1 movimento possível: mover para a terceira casa anterior!')
                    movimento = int(input('Para onde você deseja mover a carta? (3 anterior): '))
            if lista_movimentos_possiveis(baralho, posicao) == [1,3]:
                print('Você tem 2 movimento possível: ou mover para a casa anterior ou para a terceira anterior!')
                movimento = int(input('Para onde você deseja mover a carta? (primeira ou terceira anterior - 1 ou 3): '))
                while movimento != 1 and movimento != 3:
                    print('Movimento inválido')
                    print('Você tem 2 movimento possível: ou mover para a casa anterior ou para a terceira anterior!')
                    movimento = int(input('Para onde você deseja mover a carta? (1 ou 3 anterior): '))
            
            if lista_movimentos_possiveis(baralho, posicao) != []:
                resposta = carta - movimento
                emp = empilha(baralho, posicao, resposta-1)

        if len(baralho) == 1:
            print('Parabéns, você panhou!')
            jogar = input('Deseja jogar novamente? (Sim/Não) ')
            if jogar == 'nao' or jogar == 'Não':
                iniciar = False
        else:
            print("Que pena, você perdeu!")
            jogar = input('Deseja jogar novamente? (Sim/Não) ')
            if jogar == 'nao' or jogar == 'Não':
                iniciar = False

    if iniciar == False:
        return('Até a próxima!')

def cria_baralho():
    baralho = [0]
    numeros = ['A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
    naipe = ['♠','♥','♦','♣']
    
    carta_espada = []
    carta_copa = []
    carta_ouros = []
    carta_paus = []
    i = 0
    while i < len(numeros) :
        nova1 = numeros[i] + naipe[0]
        carta_espada.append(nova1)
        nova2 = numeros[i] + naipe[1]
        carta_copa.append(nova2)
        nova3 = numeros[i] + naipe[2]
        carta_ouros.append(nova3)
        nova4 = numeros[i] + naipe[3]
        carta_paus.append(nova4)
        i += 1
    baralho = carta_espada + carta_copa + carta_paus + carta_ouros
    random.shuffle(baralho)

    return baralho

def extrai_naipe(carta_no_baralho):
    if len(carta_no_baralho) == 2:
        so_naipe = carta_no_baralho[1]
    else:
        so_naipe = carta_no_baralho[2]
    return so_naipe

def extrai_valor(carta_no_baralho):
    if len(carta_no_baralho) == 2:
        so_naipe = carta_no_baralho[0]
    else:
        so_naipe = carta_no_baralho[0] + carta_no_baralho[1]
    return so_naipe

def lista_movimentos_possiveis(baralho, posicao):
    if posicao == 0:
        return[]
    elif posicao == 1:
        if extrai_valor(baralho[1]) == extrai_valor(baralho[0]) or extrai_naipe(baralho[1]) == extrai_naipe(baralho[0]):
            return[1] 
        else:
            return[]
    elif posicao == 2:
        if extrai_valor(baralho[2]) == extrai_valor(baralho[1]) or extrai_naipe(baralho[2]) == extrai_naipe(baralho[1]):
            return[1]
        else:
            return[] 
    elif (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1])) and (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-3])):
        return[1,3]
    elif (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1])):
        return[1]
    elif extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-3]):
        return[3]
    else:
        return[]

def empilha(baralho,posicao,resposta): 
    baralho[resposta] = baralho[posicao]
    del baralho[posicao]  
    return baralho

def possui_movimentos_possiveis(baralho):
    i = 0
    while i < len(baralho):
        if lista_movimentos_possiveis(baralho, i) == [1,3] or lista_movimentos_possiveis(baralho, i) == [1] or lista_movimentos_possiveis(baralho, i) == [3]:
            return True
        else:
            i+=1
    return False

main()