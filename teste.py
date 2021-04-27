# def extrai_naipe(string):
#     print(string)
#     if len(string) == 2:
#         so_naipe = string[1]
#     else:
#         so_naipe = string[2]
#     print(so_naipe)
#     return so_naipe

# def extrai_valor(string):
#     print(string)
#     if len(string) == 2:
#         so_naipe = string[0]
#     else:
#         so_naipe = string[0] + string[1]
#     print(so_naipe)
#     return so_naipe

# def possui_movimentos_possiveis(lista):
#     if lista[0]:
#         return False
#     elif lista[2] == 1:
#     if extrai_valor(lista[1]) == extrai_valor(lista[0]) or extrai_naipe(lista[1]) == extrai_naipe(lista[0]):
#         return True
#     else:
#         return False
#     elif i == 2:
#         if extrai_valor(lista[2]) == extrai_valor(lista[1]) or extrai_naipe(lista[2]) == extrai_naipe(lista[1]):
#             return True
#         else:
#             return False
#     i=3
#     while i < len(lista):

#         if (extrai_valor(lista[i]) == extrai_valor(lista[i-1]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-1])) and ((extrai_valor(lista[i]) == extrai_valor(lista[i-3]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-3]))):
#             return True
#         elif (extrai_valor(lista[i]) == extrai_valor(lista[i-1]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-1])):
#             return True
#         elif (extrai_valor(lista[i]) == extrai_valor(lista[i-3]) or extrai_naipe(lista[i]) == extrai_naipe(lista[i-3])):
#             return True
#         else:
#             return False
#         i+=1
def cria_baralho():
    baralho = []
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
    return baralho    

 
def extrai_naipe(string):
    if len(string) == 2:
        so_naipe = string[1]
    else:
        so_naipe = string[2]

    return so_naipe

def extrai_valor(string):

    if len(string) == 2:
        so_naipe = string[0]
    else:
        so_naipe = string[0] + string[1]

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

def possui_movimentos_possiveis(lista):
    i = 0
    while i < len(lista):
        if lista_movimentos_possiveis(lista,i) == [1,3] or lista_movimentos_possiveis(lista, i) == [1] or lista_movimentos_possiveis(lista, i) == [3]:
            print(lista_movimentos_possiveis(x, i))
            return True
        else:
            i+=1
    return False

lista = ['A♦', '10♥', 'Q♣', '4♠']
print(possui_movimentos_possiveis(lista))
            