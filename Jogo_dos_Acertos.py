import os
import random

def Adivinhacao():
    numero_secreto = random.randrange(1,101)
    rodada = 1
    pontos = 1000
    print(3//2)
    print(60*"=")
    print("Bem Vindo ao Jogos das Tentativas!!!")
    print(60*"=")
    print('''
        [1] Facil
        [2] Normal
        [3] Dificil 
    ''')
    print(60*"=")
    nivel = int(input("Qual dificuldade deseja: "))
    print(60*"=")
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        print(60*"=")
        chute = int(input("Digite um número entre 1 e 100: "))
        print(60*"=")

        if(chute < 1 or chute > 100):
            print("Digite um valor valído")
            print(60*"=")
            continue

        menor   = numero_secreto > chute
        acertou = numero_secreto == chute
        maior   = numero_secreto < chute

        if(acertou):
            print("Parabens!! você consegui acertar")
            print(60*"=")
            print("Você acertou e fez {} pontos!".format(pontos))
            print(60*"=")
            break

        else:
            if(maior):
                print("Ops! O número é muito alto")
                print(60*"=")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
                    print(60*"=")
            elif(menor):
                print("Eita! muito baixo")
                print(60*"=")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
                    print(60*"=")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        

    print("Fim de Jogo!!!")
    print(60*"=")


if(__name__ == "__main__"):
    Adivinhacao()