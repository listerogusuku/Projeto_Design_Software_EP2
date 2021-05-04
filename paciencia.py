# EP | Exercício Programa: Bacará Simplificado | Design de Software
# Equipe: Celina Vieira de Melo e Lister Ogusuku Ribeiro
# Data: 18/10/2020

#Descrição:
#Jogo de bacará criado com a intenção de promover uma interatividade com o usuário,
#onde este aposta em quem será o vencedor da partida (jogador, banco ou empate) e, por fim, todo
#o restante do jogo é realizado pela mesa de acordo com as regras simplificadas definidas ao longo
#do programa pelo programador.

#Neste jogo foram implementadas todas as regras avançadas.

#============================

#Importação da biblioteca "Random", que ajudará meu código a gerar números aleatórios


# print('\nPaciência Acordeão\n==================\n\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n\nExistem apenas dois movimentos possíveis:\n\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\n\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n')

# start = int(input('Digite 1 para iniciar o jogo: '))

import random

def main():
    baralho = cria_baralho() 
#    while possui_movimentos_possiveis(baralho):          
    a = 0
    while a < len(baralho):
        print('{0}. {1}'.format(a+1,baralho[a]))
        a += 1

    carta = int(input('Escolha uma carta de 1 a 52: '))
    while carta <= 0 or carta > 52:
        print('Não entendi, digite um número entre o intervalo pedido ')
    carta_no_baralho = baralho[carta-1]
    print('Sua carta é: {}'.format(carta_no_baralho))
    posicao = carta - 1 
    print(lista_movimentos_possiveis(baralho,posicao))
    posicao = carta_no_baralho

def cria_baralho():
    baralho = []
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
        print(" Você não tem movimentos possíveis")
        return baralho
    elif posicao == 1:
        if extrai_valor(baralho[1]) == extrai_valor(baralho[0]) or extrai_naipe(baralho[1]) == extrai_naipe(baralho[0]):
            print('Você tem 1 movimento possível, pode mover sua carta para a anterior') 
            resposta = input('Para onde você deseja mover a carta? ')
            if resposta != 0:
                print('Movimento inválido')     
                resposta = input('Para onde você deseja mover a carta? ') 
            else:
                return baralho_novo   
        else:
            print(" Você não tem movimentos possíveis")
            return baralho

    elif posicao == 2:
        if extrai_valor(baralho[2]) == extrai_valor(baralho[1]) or extrai_naipe(baralho[2]) == extrai_naipe(baralho[1]):
            print('Você tem 1 movimento possível, pode mover sua carta para a anterior') 
            resposta = input('Para onde você deseja mover a carta? ')
            if resposta != 1:
                print('Movimento inválido')     
                resposta = input('Para onde você deseja mover a carta? ')
            else:
                return baralho_novo   
        else:
            print(" Você não tem movimentos possíveis")
            return baralho
    elif (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1])) and (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-3])):
        print('Você tem 2 movimentos possíveis, pode mover sua carta para a anterior ou para a terceira anterior')
        resposta = input('Para onde você deseja mover a carta? ') 
        if resposta != posicao - 1 or resposta != posicao - 3:
                print('Movimento inválido')     
                resposta = input('Para onde você deseja mover a carta? ')
        else:
            print(" Você não tem movimentos possíveis")
            return baralho_novo    
      
    elif (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1])):
        print('Você tem 1 movimento possível, pode mover sua carta para a anterior')
        resposta = input('Para onde você deseja mover a carta? ') 
        if resposta != posicao - 1:
                print('Movimento inválido')     
                resposta = input('Para onde você deseja mover a carta? ')
        else:
            print(" Você não tem movimentos possíveis")
            return baralho_novo

    elif extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1]):
        print('Você tem 1 movimentos possível, pode mover sua carta para a terceira anterior')
        resposta = input('Para onde você deseja mover a carta? ') 
        if resposta != posicao - 3:
                print('Movimento inválido')     
                resposta = input('Para onde você deseja mover a carta? ')
        else:
            print(" Você não tem movimentos possíveis")
            return baralho_novo
        
    else:
        print(" Você não tem movimentos possíveis")
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