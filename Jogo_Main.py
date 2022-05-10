import Jogo_da_Forca
import Jogo_dos_Acertos
import time

def Escolhe_jogo():
    print(3//2)
    print(60*"=")
    print("Bem Vindo ao Menu de Jogos!!!")
    print(60*"=")
    print('''
        [1] Adivinhação
        [2] Forca
    ''')
    option = int(input("Qual você deseja jogar? "))
    print(60*"=")

    if option == 1:
        print("Inicializando o Jogo das Adivinhações...")
        print(60*"=")
        time.sleep(2)
        Jogo_dos_Acertos.Adivinhacao()

    elif option == 2:
        print("Inicializando o Jogo da Forca...")
        print(60*"=")
        time.sleep(2)
        Jogo_da_Forca.Forca()

if(__name__ == "__main__"):
    Escolhe_jogo()