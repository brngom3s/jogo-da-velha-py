tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
opcao = 0
j1 = 0
j2 = 0
cd1 = 0
cd2 = 0
jogadas = 0
jogador1 = True
jogador2 = True
escolhido = True

while opcao != 3:
    if jogadas == 9:
        print("Deu velha!")
        break
    print("------- Bem vindo ao nosso jogo! -------")
    print("Digite uma opção referente ao que deseja fazer: ")
    print("[1] Player 1 joga.")
    print("[2] Player 2 joga.")
    print("[3] Sair do programa.")
    opcao = int(input("Digite a opção: "))
    if opcao == 1 and jogador1 == True:
        print("Esse será o tabuleiro do nosso jogo: ")
        for L in range(1):
            print()
            print("    ", "0 ", " 1 ", " 2  ")
            print()
            print("0  ", "", tabuleiro[0][0], "|",
                  tabuleiro[0][1], "|", tabuleiro[0][2])
            print("   ", "---|---|---")
            print("1  ", "", tabuleiro[1][0], "|",
                  tabuleiro[1][1], "|", tabuleiro[1][2])
            print("   ", "---|---|---")
            print("2  ", "", tabuleiro[2][0], "|",
                  tabuleiro[2][1], "|", tabuleiro[2][2])
            print()

        while escolhido == True:
            escolha = input(
                "Para começar bem, vamos deixar que o 1º jogador decida sua marcação, entre [X] e [O]: ")
            if escolha == "X" or escolha == "x" and escolhido == True:
                print(
                    f"Isso aí, o 1º player será [X], logo o 2º player será [O].")
                escolhido = False
                j1 = "X"
                j2 = "O"
            elif escolha == "O" or escolha == "o" and escolhido == True:
                print(
                    f"Isso aí, o 1º player será [O], logo o 2º player será [X].")
                escolhido = False
                j1 = "O"
                j2 = "X"
        j1jogar = False

        while j1jogar == False:
            print("Jogador 1, faça sua jogada!")
            cd1 = int(input("Digite a coordenada da linha: "))
            cd2 = int(input("Digite a coordenada da coluna: "))
            while cd1 < 0 or cd1 > 2 or cd2 < 0 or cd2 > 2:
                print("Coordenada inválida, digite novamente!")
                cd1 = int(input("Digite a coordenada da linha: "))
                cd2 = int(input("Digite a coordenada da coluna: "))
            if tabuleiro[cd1][cd2] == j1 or tabuleiro[cd1][cd2] == j2:
                print("Esta coordenada já está ocupada. Tente novamente!")
            else:
                tabuleiro[cd1][cd2] = j1
                j1jogar = True
                jogador1 = False
                jogador2 = True
                jogadas += 1
        for L in range(1):
            print()
            print("    ", "0 ", " 1 ", " 2  ")
            print()
            print("0  ", "", tabuleiro[0][0], "|",
                  tabuleiro[0][1], "|", tabuleiro[0][2])
            print("   ", "---|---|---")
            print("1  ", "", tabuleiro[1][0], "|",
                  tabuleiro[1][1], "|", tabuleiro[1][2])
            print("   ", "---|---|---")
            print("2  ", "", tabuleiro[2][0], "|",
                  tabuleiro[2][1], "|", tabuleiro[2][2])
            print()
        if ((tabuleiro[0][0] == j1 and tabuleiro[0][1] == j1 and tabuleiro[0][2] == j1) or
           (tabuleiro[1][0] == j1 and tabuleiro[1][1] == j1 and tabuleiro[1][2] == j1) or
           (tabuleiro[2][0] == j1 and tabuleiro[2][1] == j1 and tabuleiro[2][2] == j1) or
           (tabuleiro[0][0] == j1 and tabuleiro[1][0] == j1 and tabuleiro[2][0] == j1) or
           (tabuleiro[0][1] == j1 and tabuleiro[1][1] == j1 and tabuleiro[2][1] == j1) or
           (tabuleiro[0][2] == j1 and tabuleiro[1][2] == j1 and tabuleiro[2][2] == j1) or
           (tabuleiro[0][0] == j1 and tabuleiro[1][1] == j1 and tabuleiro[2][2] == j1) or
           (tabuleiro[0][2] == j1 and tabuleiro[1][1] == j1 and tabuleiro[2][0] == j1)):
            print("Parabens! Jogador 1 venceu!")
            break

    elif opcao == 2 and jogador2 == True:
        for L in range(1):
            print()
            print("    ", "0 ", " 1 ", " 2  ")
            print()
            print("0  ", "", tabuleiro[0][0], "|",
                  tabuleiro[0][1], "|", tabuleiro[0][2])
            print("   ", "---|---|---")
            print("1  ", "", tabuleiro[1][0], "|",
                  tabuleiro[1][1], "|", tabuleiro[1][2])
            print("   ", "---|---|---")
            print("2  ", "", tabuleiro[2][0], "|",
                  tabuleiro[2][1], "|", tabuleiro[2][2])
            print()

        while escolhido == True:
            escolha = input(
                "Para começar bem, vamos deixar que o 1º jogador decida sua marcação, entre [X] e [O]: ")
            if escolha == "X" or escolha == "x" and escolhido == True:
                print(
                    f"Isso aí, o 2º player será [X], logo o 1º player será [O].")
                j1 = "O"
                j2 = "X"
                escolhido = False
            elif escolha == "O" or escolha == "o" and escolhido == True:
                print(
                    f"Isso aí, o 1º player será [O], logo o 2º player será [X].")
                j1 = "X"
                j2 = "O"
                escolhido = False

        j2jogar = False
        while j2jogar == False:
            print("Jogador 2, faça sua jogada!")
            cd1 = int(input("Digite a coordenada da linha: "))
            cd2 = int(input("Digite a coordenada da coluna: "))
            while cd1 < 0 or cd1 > 2 or cd2 < 0 or cd2 > 2:
                print("Coordenada inválida, digite novamente!")
                cd1 = int(input("Digite a coordenada da linha: "))
                cd2 = int(input("Digite a coordenada da coluna: "))
            if tabuleiro[cd1][cd2] == j1 or tabuleiro[cd1][cd2] == j2:
                print("Esta coordenada já está ocupada. Tente novamente!")
            else:
                tabuleiro[cd1][cd2] = j2
                j2jogar = True
                jogador2 = False
                jogador1 = True
                jogadas += 1
            print()
            print("    ", "0 ", " 1 ", " 2  ")
            print()
            print("0  ", "", tabuleiro[0][0], "|",
                  tabuleiro[0][1], "|", tabuleiro[0][2])
            print("   ", "---|---|---")
            print("1  ", "", tabuleiro[1][0], "|",
                  tabuleiro[1][1], "|", tabuleiro[1][2])
            print("   ", "---|---|---")
            print("2  ", "", tabuleiro[2][0], "|",
                  tabuleiro[2][1], "|", tabuleiro[2][2])
            print()

        if ((tabuleiro[0][0] == j2 and tabuleiro[0][1] == j2 and tabuleiro[0][2] == j2) or
           (tabuleiro[1][0] == j2 and tabuleiro[1][1] == j2 and tabuleiro[1][2] == j2) or
           (tabuleiro[2][0] == j2 and tabuleiro[2][1] == j2 and tabuleiro[2][2] == j2) or
           (tabuleiro[0][0] == j2 and tabuleiro[1][0] == j2 and tabuleiro[2][0] == j2) or
           (tabuleiro[0][1] == j2 and tabuleiro[1][1] == j2 and tabuleiro[2][1] == j2) or
           (tabuleiro[0][2] == j2 and tabuleiro[1][2] == j2 and tabuleiro[2][2] == j2) or
           (tabuleiro[0][0] == j2 and tabuleiro[1][1] == j2 and tabuleiro[2][2] == j2) or
           (tabuleiro[0][2] == j2 and tabuleiro[1][1] == j2 and tabuleiro[2][0] == j2)):
            print("Parabens! Jogador 2 venceu!")
            break

    elif opcao == 3:
        print("Programa finalizado!")
    elif jogador1 == False or jogador2 == False:
        if jogador1 == False:
            print()
            print("Você já jogou agora é a vez do outro player 2!!!")
            print()
        else:
            print()
            print("Você já jogou agora é a vez do outro player 1!!!")
    else:
        print("Digite uma opção válida!")
