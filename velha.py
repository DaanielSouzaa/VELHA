import random


def velha_s(player):
    matriz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    xo = 'O'
    printa(matriz)
    while True:
        marca = 20
        while marca not in range(1, 10):
            marca = int(input("Digite o número da casa desejada: "))
            if marca == 123456789:
                for i in range(0, 9):
                    matriz[i] = xo
                printa(matriz)
                verifica(matriz)
            elif matriz[marca - 1] == 'X':
                marca = 20
        for j in range(0, 9):
            if matriz[j] == marca:
                matriz[j] = xo
                printa(matriz)
                verifica(matriz)
                if xo == 'O':
                    if matriz[0] == matriz[1] and matriz[2] == 3: 
                        matriz[2] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[8] and matriz[4] == 5: 
                        matriz[4] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[6] == matriz[0] and matriz[3] == 4: 
                        matriz[3] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[2] and matriz[1] == 2: 
                        matriz[1] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[4] == matriz[5] and matriz[3] == 4:
                        matriz[3] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[4] and matriz[8] == 9:
                        matriz[8] = 'X'                    
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[2] == matriz[5] and matriz[8] == 9:
                        matriz[8] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[3] and matriz[6] == 7: 
                        matriz[6] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[6] and matriz[3] == 4:
                        matriz[3] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[1] == matriz[2] and matriz[0] == 1: 
                        matriz[0] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[1] == matriz[4] and matriz[7] == 8: 
                        matriz[7] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[2] == matriz[4] and matriz[6] == 7: 
                        matriz[6] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[3] == matriz[4] and matriz[5] == 6: 
                        matriz[5] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[3] == matriz[6] and matriz[0] == 1: 
                        matriz[0] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[4] == matriz[6] and matriz[2] == 3: 
                        matriz[2] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[5] == matriz[8] and matriz[2] == 3: 
                        matriz[2] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[6] == matriz[7] and matriz[8] == 9:
                        matriz[8] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[6] == matriz[8] and matriz[7] == 8: 
                        matriz[7] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[8] and matriz[4] == 5: 
                        matriz[4] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[7] == matriz[4] and matriz[1] == 2: 
                        matriz[1] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[2] == matriz[6] and matriz[0] == 1: 
                        matriz[0] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[8] == matriz[7] and matriz[6] == 7: 
                        matriz[6] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[8] and matriz[5] == 6: 
                        matriz[5] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[2] == matriz[6] and matriz[5] == 6: 
                        matriz[5] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    elif matriz[0] == matriz[8] and matriz[3] == 4:
                        matriz[3] = 'X'
                        printa(matriz)
                        verifica(matriz)
                        break
                    else:
                        for i in range(0, 9):
                            if matriz[i] != 'X' and matriz[i] != 'O':
                                matriz[i] = 'X'
                                printa(matriz)
                                verifica(matriz)
                                break


def velha_m(player):
    xo_1 = 0
    xo_2 = 0
    matriz = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        while xo_1 != 'X'and xo_1 != 'O':
            xo_1 = input("Jogador 1 'X' ou 'O'? ")
        if xo_1 == 'X':
            xo_2 = 'O'
        else:
            xo_2 = 'X'
        print(f'JOGADOR 1: {xo_1} | JOGADOR 2: {xo_2}')
        printa(matriz)
        marca_1 = 20
        marca_2 = 20
        while marca_1 not in range(1, 10):
            print('PRIMEIRO JOGADOR')
            marca_1 = int(input("Digite o número da casa desejada: "))
        for i in range(0, 9):
            if marca_1 == matriz[i]:
                matriz[i] = xo_1
                printa(matriz)
                verifica(matriz)
                break
        while marca_2 not in range(1, 10):
            print('SEGUNDO JOGADOR')
            marca_2 = int(input("Digite o número da casa desejada: "))
        for i in range(0, 9):
            if marca_2 == matriz[i]:
                matriz[i] = xo_2
                printa(matriz)
                verifica(matriz)
                break


def verifica(matriz):
    ### EASTEREGG ###
    if matriz[0] == matriz[1]:
        if matriz[0] == matriz[2]:
            if matriz[0] == matriz[3]:
                if matriz[0] == matriz[4]:
                    if matriz[0] == matriz[5]:
                        if matriz[0] == matriz[6]:
                            if matriz[0] == matriz[7]:
                                if matriz[0] == matriz[8]:
                                    print('CARAI CHEFE, BRAAAABO!')
                                    inicio()

    ### EASTEREGG ###

    ### Horizontal ###
    if matriz[0] == matriz[1] and matriz[0] == matriz[2]:
        print(f'{matriz[0]} venceu!')
        inicio()
    elif matriz[3] == matriz[4] and matriz[3] == matriz[5]:
        print(f'{matriz[3]} venceu!')
        inicio()
    elif matriz[6] == matriz[7] and matriz[6] == matriz[8]:
        print(f'{matriz[6]} venceu!')
        inicio()
    ### Horizontal ###

    ### Vertical ###
    elif matriz[2] == matriz[5] and matriz[2] == matriz[8]:
        print(f'{matriz[2]} venceu!')
        inicio()
    elif matriz[1] == matriz[4] and matriz[1] == matriz[7]:
        print(f'{matriz[1]} venceu!')
        inicio()
    elif matriz[0] == matriz[3] and matriz[0] == matriz[6]:
        print(f'{matriz[0]} venceu!')
        inicio()
    ### Vertical ###
    ### Diagonais ###
    elif matriz[2] == matriz[4] and matriz[2] == matriz[6]:
        print(f'{matriz[2]} venceu!')
        inicio()
    elif matriz[0] == matriz[4] and matriz[0] == matriz[8]:
        print(f'{matriz[0]} venceu!')
        inicio()
    ### Diagonais ###

    ### VELHA ###
    if matriz[0] == 'X' or matriz[0] == 'O':
        if matriz[1] == 'X' or matriz[1] == 'O':
            if matriz[2] == 'X' or matriz[2] == 'O':
                if matriz[3] == 'X' or matriz[3] == 'O':
                    if matriz[4] == 'X' or matriz[4] == 'O':
                        if matriz[5] == 'X' or matriz[5] == 'O':
                            if matriz[6] == 'X' or matriz[6] == 'O':
                                if matriz[7] == 'X' or matriz[7] == 'O':
                                    if matriz[8] == 'X' or matriz[8] == 'O':
                                        print('VELHA!')
                                        inicio()
    ### VELHA ###


def printa(matriz):
    print("---------- JOGO VELHA ----------")
    print(f"""            |        |
        {matriz[0]}   |    {matriz[1]}   |    {matriz[2]}
    ________|________|________
            |        |
        {matriz[3]}   |    {matriz[4]}   |    {matriz[5]}
    ________|________|________
            |        |
        {matriz[6]}   |    {matriz[7]}   |    {matriz[8]}      
            |        |""")


def inicio():
    print("Começando jogo, por favor escolha a quantidade de jogadores:")
    player = int(
        input("Opções:\n 1 para singleplayer:\n 2 para multiplayer: \n 3 para sair "))
    if player == 1:
        velha_s(player)
    elif player == 2:
        velha_m(player)
    else:
        exit()


inicio()
