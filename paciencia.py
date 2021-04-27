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
def cria_baralho():
    baralho= []
    numeros = ['A', '2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
    naipe=['♠','♥','♦','♣']
    
    # num_total_cartas = 52
    carta_espada= []
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
    a = 0
    while a < len(baralho):
        print('{0}. {1}'.format(a+1,baralho[a]))
        a += 1

    carta = int(input('Escolha uma carta de 1 a 52: '))
    while carta <= 0 or carta > 52:
        print('Não entendi, digite um número entre o intervalo pedido ')
    carta_no_baralho = baralho[carta-1]
    print('Sua carta é: {}'.format(carta_no_baralho))
    
    return baralho

cria_baralho()


