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


print('\nPaciência Acordeão\n==================\n\nSeja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n\nExistem apenas dois movimentos possíveis:\n\n1. Empilhar uma carta sobre a carta imediatamente anterior;\n2. Empilhar uma carta sobre a terceira carta anterior.\n\nPara que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n\n1. As duas cartas possuem o mesmo valor ou \n2. As duas cartas possuem o mesmo naipe.\nDesde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n')

start = int(input('Digite 1 para iniciar o jogo: '))

import random

baralho=['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K']  # Criação de uma lista com os índices do baralho.
naipe=['Ouro','Paus','Copas','Espada']





# Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

# 1. As duas cartas possuem o mesmo valor ou 
# 2. As duas cartas possuem o mesmo naipe. 

# Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

# Aperte [Enter] para iniciar o jogo...