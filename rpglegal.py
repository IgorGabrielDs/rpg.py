import pick
from pick import pick

#Variaveis globais
nome = "..."
vida = 10
classe = "..."
ataques = {}

def erro():
    print("Tente novamente...\n")

def status():
    global nome
    global vida
    global ataques
    print(f" Nome: {nome} Vida: {vida} Classe: {classe}")


def criacao_personagem():
    global nome 
    global classe
    while True:
        nome = str(input("Digite seu nome: ")).strip().capitalize()

        if nome != "":
            break
        else:
            nome = "..."
            erro()
    classe = ['Guerreiro', 'Mago', 'Ladrão', 'Mendigo']
    classe, index = pick(classe, "Selecione sua classe")
    print(classe)

criacao_personagem()
status()