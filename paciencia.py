# EP | Exercício Programa: Paciência de Acordeão | Design de Software
# Equipe: Celina Vieira de Melo e Lister Ogusuku Ribeiro
# Data: 05/05/2021

# Descrição:
# Jogo paciência acordeão criado com a intenção de promover uma interatividade com o usuário.

# Neste jogo foram implementadas todas as regras avançadas.

# ============================

print('\nPaciência Acordeão\n==================\n\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n\nExistem apenas dois movimentos possíveis:\n\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\n\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n')

import random

def main():
    baralho = cria_baralho() 
    while possui_movimentos_possiveis(baralho):          
        a = 0
        while a < len(baralho):
            print('{0}. {1}'.format(a+1,baralho[a]))
            a += 1

        carta = int(input('Escolha uma carta: '))

        carta_no_baralho = baralho[carta-1]
        print('Sua carta é: {}'.format(carta_no_baralho))
        posicao = carta - 1 
        print(lista_movimentos_possiveis(baralho,posicao))
        resposta = int(input('Para onde você deseja mover a carta? '))
        emp = empilha(baralho, posicao, resposta-1)

        if possui_movimentos_possiveis(baralho) == False:
            print('Você perdeu!')
        else:
            print('Parabéns, você ganhou!')

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
    elif extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1]):
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

x = main()
print(x)